import logging
import json
import requests
from pathlib import Path
from dotenv import dotenv_values

app_dir = Path(__file__).resolve().parent
creds = dotenv_values(f"{app_dir}/.env")
webhook: str = creds['MSTEAMS_WEBHOOK']

logger = logging.getLogger(__name__)

def run(alert: dict, correlation_msg: str, options: dict) -> None:
    logger.debug("run: init")

    text = ""
    if correlation_msg:
        text: str = f" -> {correlation_msg}"

    title = f"**Wazuh Alert - ({alert['rule']['id']}) {alert['rule']['description']} - Level {alert['rule']['level']}{text}**"

    if 'agent' in alert:
        agent_info = f"({alert['agent']['id']}) - {alert['agent']['name']} - {alert['agent']['ip']}"
    if 'agentless' in alert:
        agent_info = f"Agentless Host {alert['agentless']['host']}"

    msg = f"{title}:\n\n{agent_info}\n\n{alert['rule']['groups']}"
    attach = json.dumps({ "text": msg })

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    res = requests.post(webhook, data=attach, headers=headers)
    logger.debug(res.text)
