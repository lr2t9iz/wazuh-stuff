import requests
import json

import logging
logger = logging.getLogger(__name__)

from pathlib import Path
from dotenv import dotenv_values

app_dir = Path(__file__).resolve().parent
creds = dotenv_values(f"{app_dir}/.env")

wapi_url = creds['WAPI_URL']
wapi_user = creds['WAPI_USER']
wapi_pass = creds['WAPI_PASS']

# https://documentation.wazuh.com/current/user-manual/api/reference.html
token = requests.post(f"{wapi_url}/security/user/authenticate", verify=False,
                                 auth=requests.auth.HTTPBasicAuth(wapi_user, wapi_pass))
token = token.json()
token = token['data']['token']

def response(agent_id, command_r) -> None:
    headers = { "Authorization": f"Bearer {token}", "Content-Type": "application/json" }
    body = { "command": "!semishell.exe", "arguments": [command_r] }
    ar = requests.put(f"{wapi_url}/active-response?agents_list={agent_id}", verify=False,
                    headers=headers, data=json.dumps(body) )
    logger.debug(ar.json())
