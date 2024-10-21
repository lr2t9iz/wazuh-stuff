#!/var/ossec/framework/python/bin/python3
# c-137 Labs (2024.10.20) -> wazuh script modified
# This integration uses Microsoft Teams incoming webhooks and allows security professionals to receive real-time alerts directly within designated channels.

import sys
import json
import time
import os

try:
    import requests
    from requests.auth import HTTPBasicAuth
except Exception as e:
    print("No module 'requests' found. Install: pip install requests")
    sys.exit(1)

debug_enabled = False
app_dir = os.path.dirname(os.path.realpath(__file__))
# wazuh dir /var/ossec/
wazuh_dir = os.path.dirname(app_dir)
json_alert = {}
now = time.strftime("%a %b %d %H:%M:%S %Z %Y")

# integration log
log_file = f"{wazuh_dir}/logs/integrations.log"

def debug(msg):
    if debug_enabled:
        msg = f"{now}: {msg}\n"
        print(msg)
        with open(log_file, "a") as f:
            f.write(msg)

def send_msg(msg, url):
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    res = requests.post(url, data=msg, headers=headers)
    debug(res.text)

def generate_msg(alert):
    title = f"**Wazuh Alert - ({alert['rule']['id']}) {alert['rule']['description']} - Level {alert['rule']['level']}**"
    if 'agent' in alert:
        agent_info = f"({alert['agent']['id']}) - {alert['agent']['name']} - {alert['agent']['ip']}"
    if 'agentless' in alert:
        agent_info = f"Agentless Host {alert['agentless']['host']}"

    msg = f"{title}:\n\n{agent_info}\n\n{alert['rule']['groups']}"
    attach = { "text": msg }
    return json.dumps(attach)

def main(alert_file_location, webhook):
    debug("# Starting")
    debug("# Webhook")
    debug(webhook)
    debug("# File location")
    debug(alert_file_location)

    # Load alert. Parse JSON object.
    with open(alert_file_location) as alert_file:
        json_alert = json.load(alert_file)
    debug("# Processing alert")
    debug(json_alert)

    debug("# Generating message")
    msg = generate_msg(json_alert)
    debug(msg)

    debug("# Sending message")
    send_msg(msg, webhook)

if __name__ == "__main__":
    try:
        # Read arguments
        bad_arguments = False
        if len(sys.argv) >= 4:
            alert_f  = sys.argv[1]
            api_key  = sys.argv[2]
            hook_url = sys.argv[3]
            debug_e  = sys.argv[4] if len(sys.argv) > 4 else ''

            msg = f"{now} {alert_f} {api_key} {hook_url} {debug_e}"
            debug_enabled = (debug_e == 'debug')
        else:
            msg = f"{now} Wrong arguments"
            bad_arguments = True

        # Logging the call
        with open(log_file, 'a') as f:
            f.write(msg + '\n')

        if bad_arguments:
            debug("# Exiting: Bad arguments.")
            sys.exit(1)

        # Main function
        main(alert_f, hook_url)

    except Exception as e:
        debug(str(e))
        raise

# chmod 750 /var/ossec/integrations/custom-xmsteams
# chown root:wazuh /var/ossec/integrations/custom-xmsteams

# ossec.conf configuration:
#  <integration>
#      <group>syscheck_file</group>
#      <name>custom-xmsteams</name>
#      <hook_url>https://YYYYY.office.com/AAAA/XXXXXXXXXXXXXX</hook_url>
#      <alert_format>json</alert_format>
#  </integration>
