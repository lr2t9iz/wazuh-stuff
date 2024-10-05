from wazuh_indexer import extract_data, load_result
import pandas as pd
from rules import get_multiples_failed_logon

def get_df4625():
    fields = ["timestamp", "data.win.eventdata.ipAddress", 
            "data.win.eventdata.targetUserName", "data.win.system.computer"] # SELECT
    index_pattern = "wazuh-alerts-*" # FROM
    query_dsl = {  # WHERE
            "bool": {
            "filter": [
                { "range": { "timestamp": { "gt": "now/m-3h" } } }, # DATA batch
                { "terms": { "data.win.system.eventID": ["4625"] } },
                { "exists": { "field": "data.win.eventdata.ipAddress" } }
            ],
            "must_not": [
                { "terms": { "data.win.eventdata.ipAddress": ["127.0.0.1"] } } #, { "wildcard": { "user.name": "*$" } }
            ]
        }
    }
    size = 10000 # LIMIT
    sort_docs = [ { "timestamp": { "order": "desc" } } ] # ORDER by

    query = { 
            "_source": { "includes": fields },
            "query": query_dsl,
            "size": size, 
            "sort": sort_docs
        }

    docs =  extract_data(index_pattern, query) # TODB
    data = []
    if docs:
        df = pd.json_normalize(docs)
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_localize(None)
        df.rename(columns={"data.win.eventdata.ipAddress": "SourceIP"}, inplace=True)
        df.rename(columns={"data.win.eventdata.targetUserName": "UserName"}, inplace=True)
        df.rename(columns={"data.win.system.computer": "HostName"}, inplace=True)
        return df
    return None

def get_list4624(events):
    incidents = []
    for logon in events:
        fields = ["timestamp", "data.win.eventdata.ipAddress", 
                "data.win.eventdata.targetUserName", "data.win.system.computer",
                ] # SELECT
        index_pattern = "wazuh-alerts-*" # FROM
        query_dsl = {  # WHERE
                "bool": {
                "filter": [
                    { "range": { "timestamp": { "gt": logon['timestamp'], "lt": logon['UntilTimestamp']  } } }, # DATA batch
                    { "term": { "data.win.system.eventID": "4624" } },
                    { "term": { "data.win.eventdata.ipAddress": logon['SourceIP'] } },
                    { "term": { "data.win.eventdata.targetUserName": logon['UserName'] } },
                    { "term": { "data.win.system.computer": logon['HostName'] } }
                ] #, "must_not": [ ] exceptions
            }
        }
        size = 10000 # LIMIT
        sort_docs = [ { "timestamp": { "order": "desc" } } ] # ORDER by
        
        query = { 
                "_source": { "includes": fields },
                "query": query_dsl,
                "size": size, 
                "sort": sort_docs
            }
        
        docs = extract_data(index_pattern, query) # TODB
        if docs:
            for doc in docs:
                doc['until_timestamp'] = logon['UntilTimestamp']
                doc['failed_logon'] = logon['Attempts']
                doc['rule_name'] = "failed_logins_followed_by_successful_login"
                incidents.append(doc)
    return incidents

def main():
    failed_logon = get_df4625()
    events = get_multiples_failed_logon(failed_logon)
    incidents = get_list4624(events)
    if incidents:
        load_result("wazuh-anomaly-detection", incidents) # save results

main()