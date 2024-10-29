import requests
import json
import logging
from pathlib import Path
from dotenv import dotenv_values
from datetime import datetime

app_dir = Path(__file__).resolve().parent
creds = dotenv_values(f"{app_dir}/.env")
wi_url  = creds['WI_URL']
wi_user = creds['WI_USER']
wi_pass = creds['WI_PASS']

logger = logging.getLogger(__name__)

today = datetime.today()

index_intel = "wazuh-intel"
index_pattern = f"wazuh-intel-*"
def extract_data(query: dict) -> list:
    docs = requests.get(f"{wi_url}/{index_pattern}/_search", verify=False,
                        auth=requests.auth.HTTPBasicAuth(wi_user, wi_pass),
                        json=query)
    docs = docs.json()['hits']['hits']
    data = []
    if docs:
        data = [doc['_source'] for doc in docs]
    return data

def load_result(result: dict) -> None:
    index_dr = f"{index_intel}-{today.year}.{today.month}"
    postinfo = requests.post(f"{wi_url}/{index_dr}/_doc/", verify=False,
                            auth=requests.auth.HTTPBasicAuth(wi_user, wi_pass),
                            headers = {'Content-Type': 'application/json'},
                            data=json.dumps(result))
