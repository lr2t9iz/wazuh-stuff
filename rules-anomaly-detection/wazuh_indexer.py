import os
from dotenv import dotenv_values
import requests, json
from datetime import datetime
import urllib3
urllib3.disable_warnings()

app_dir = os.getcwd()
creds = dotenv_values(f"{app_dir}/.env")

wi_url = creds['WI_URL']
wi_user = creds['WI_USER']
wi_pass = creds['WI_PASS']

def extract_data(index_pattern, query):
    docs = requests.get(f"{wi_url}/{index_pattern}/_search", verify=False,
                        auth=requests.auth.HTTPBasicAuth(wi_user, wi_pass),
                        json=query)
    docs = docs.json()['hits']['hits']
    data = []
    if docs:
        data = [doc['_source'] for doc in docs]
    return data

def load_result(index_pattern, results):
    today = datetime.today()
    index_pattern = f"{index_pattern}-{today.year}.{today.month}"
    postinfo = {}
    for result in results:
        postinfo = requests.post(f"{wi_url}/{index_pattern}/_doc/", verify=False,
                            auth=requests.auth.HTTPBasicAuth(wi_user, wi_pass),
                            headers = {'Content-Type': 'application/json'},
                            data=json.dumps(result))
    return postinfo.json()
