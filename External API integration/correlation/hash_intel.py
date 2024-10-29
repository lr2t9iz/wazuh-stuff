import logging
import sys
from pathlib import Path
from datetime import datetime

app_dir = Path(__file__).resolve().parent
sys.path.append(str(app_dir.parent))
from utils import virustotal as vt
from utils import wazuh_indexer as wi
from utils import wazuh_socket as ws

logger = logging.getLogger(__name__)

def run(alert: dict) -> str:
    logger.debug("run: init")
    filehash: str = ""
    alert_output: dict = {}
    if 'syscheck' in alert and alert['syscheck']['md5_after']:
        filehash = alert['syscheck']['md5_after']
    else:
        return ""

    localinfo: list = wi.extract_data({ "query": { "bool": { "filter": [ { "term": { "virustotal.source.md5": filehash } } ] } } })
    if localinfo:
        logger.debug(f"localinfo: {localinfo[0]}")
        alert_output = localinfo[0]
    else:
        alert_output = vt.get_fileinfo(filehash)
        logger.debug(f"alert_output: {alert_output}")
        alert_output['virustotal']['source'] = {
                'md5':      alert['syscheck']['md5_after'],
                'sha1':     alert['syscheck']['sha1_after']
                }
        alert_output['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        wi.load_result(alert_output)
    alert_output['virustotal']['source']['alert_id'] =  alert['id']
    alert_output['virustotal']['source']['file'] = alert['syscheck']['path']

    ws.send_msg(alert_output, alert['agent'])
    if  'positives' in alert_output['virustotal'] and  alert_output['virustotal']['positives'] > 0:
        return str(alert_output['virustotal']['permalink'])
    else:
        return ""
