import sys
import logging
logger = logging.getLogger(__name__)

from pathlib import Path
app_dir = Path(__file__).resolve().parent
sys.path.append(str(app_dir.parent))
from utils import wazuh_api as wa

def run(alert: dict, correlation_msg: str, options: dict) -> None:
    logger.debug(f"run: init")
    if correlation_msg:
        agentid = alert['agent']['id']
        filepath = alert['syscheck']['path']
        logger.debug(filepath)
        procname = Path(filepath.replace("\\", "/")).name
        logger.debug(procname)
        cmd = f"cmd /c taskkill /f /im \"{procname}\" & del /f \"{filepath}\""
        wa.response(agentid, cmd)

