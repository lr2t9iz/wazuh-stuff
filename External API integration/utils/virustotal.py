import requests
import json
import logging
from pathlib import Path
from dotenv import dotenv_values
from datetime import datetime

app_dir = Path(__file__).resolve().parent
creds = dotenv_values(f"{app_dir}/.env")
vt_token: str = creds['VT_TOKEN']

logger = logging.getLogger(__name__)

def get_fileinfo(file_hash: str) -> dict:
    headers = {"accept": "application/json", "x-apikey": f"{vt_token}"}
    response = requests.get(f"https://www.virustotal.com/api/v3/files/{file_hash}",
                        headers=headers)
    alert_output = {'virustotal': {}, 'integration': 'virustotal'}

    if response.status_code == 200:
        alert_output['virustotal']['found'] = 1
        alert_output['virustotal']['malicious'] = 0

        fileinfo = response.json()['data']
        fileinfo_attr = fileinfo['attributes']
        if fileinfo_attr['last_analysis_stats']['malicious'] > 0:
            alert_output['virustotal']['malicious'] = 1
        alert_output['virustotal']['sha1'] = fileinfo_attr['sha1']
        if 'creation_date' in fileinfo_attr:
            alert_output['virustotal']['creation_date'] = datetime.utcfromtimestamp(
                    fileinfo_attr['creation_date']).isoformat() + 'Z'
        alert_output['virustotal']['positives'] = fileinfo_attr['last_analysis_stats']['malicious']
        alert_output['virustotal']['total'] = (fileinfo_attr['last_analysis_stats']['malicious'] +
                fileinfo_attr['last_analysis_stats']['undetected'])
        alert_output['virustotal']['permalink'] = f"https://www.virustotal.com/gui/file/{fileinfo['id']}"

    else:
        if response.status_code == 404: #vt.v3
            alert_output['virustotal']['found'] = 0
            alert_output['virustotal']['description'] = 'Error: File Hash not found'
        elif response.status_code == 204:
            alert_output['virustotal']['error'] = response.status_code
            alert_output['virustotal']['description'] = 'Error: Public API request rate limit reached'
        elif response.status_code == 401:
            alert_output['virustotal']['error'] = 403 #vt.v2
            alert_output['virustotal']['description'] = 'Error: Wrong API key'
        elif response.status_code == 408:
            alert_output['virustotal']['error'] = response.status_code
            alert_output['virustotal']['description'] = 'Error: API request timed out'
        else:
            alert_output['virustotal']['error'] = response.status_code
            alert_output['virustotal']['description'] = 'Error: API request fail'
    return alert_output

#print(get_fileinfo('e4968ef99266df7c9a1f0637d2389dab'))
