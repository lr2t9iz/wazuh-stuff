# WAZUH - Use Cases Integrator [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/mit/)

## Overview

Wazuh XDR use cases' integrator scripts 

### Rule ID
- Wazuh Rule [between 0 and 99999]
- Custom Rule [between 100000 and 120000](https://documentation.wazuh.com/current/user-manual/ruleset/custom.html#adding-new-decoders-and-rules)
  - Custom Integrator Rule [`between 110000 and 120000`][::10]

* [Prerequisites](#prerequisites)
* [Usage](#usage---deploying)
* [Wazuh Utils](#wazuh-utils)
* [Wazuh Capabilities](#wazuh-capabilities)
* [Wazuh Integrations](#wazuh-integration)
* [References](#refences)

## Prerequisites
- Have Wazuh Installed [Installation Guide](https://documentation.wazuh.com/current/deployment-options/index.html) or [Wazuh Docker Bundle](https://github.com/lr2t9iz/wazuh-docker-bundle)

- Groups creation on Wazuh Dashobard
  - `w1ndows_s0urces` for Windows Endpoint
  - `l1nux_s0urces` for Linux Endpoint

- Have an agent deployed and added to the group [reference](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/index.html)
For make changes and command monitoring (remote commands execution) on agent, enable `remote_commands` for each agents [reference](https://documentation.wazuh.com/current/user-manual/capabilities/command-monitoring/how-it-works.html)
```
# Windows Agent
## C:\Program Files (x86)\ossec-agent\local_internal_options.conf
# Linux Agent
## /var/ossec/etc/local_internal_options.conf
logcollector.remote_commands=1
```
- Configuration - Create the `.env` file for credentials. Take .env-example as reference
## Usage - Deploying
- clone repo into wazuh server(manager) and exec the following command.
```bash
# configuration for windows endpoint
bash deploy_for.sh windows
# configuration for linux edpoint
bash deploy_for.sh linux
```

## Wazuh Utils
- [Wazuh Email CSVReporting](https://github.com/lr2t9iz/wazuh-email-csvreporting)
- [Wazuh Indexer Rollup](https://github.com/lr2t9iz/wazuh-indexer-rollup)

## Wazuh Capabilities

### wc001 - Vulnerability detection
- [How it works](https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/how-it-works.html)

### wc002 - System inventory
- [How it works](https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/how-it-works.html)

### wc003 - Security Configuration Assessment (SCA)
- [How it works](https://documentation.wazuh.com/current/user-manual/capabilities/sec-config-assessment/how-it-works.html)
- [SCA - blog](https://wazuh.com/blog/security-configuration-assessment/)

### wc004 - File integrity monitoring (FIM)
- [How it works](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/how-it-works.html)

### wc005 - Log data collection
- [How it works](https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/how-it-works.html)

### wc006 - Command monitoring
- [How it works](https://documentation.wazuh.com/current/user-manual/capabilities/command-monitoring/how-it-works.html)

### wc007 - Active Response
- Pending

### wc008 - Osquery
- [How it works](https://documentation.wazuh.com/current/user-manual/capabilities/osquery.html#how-it-works)

## Wazuh Integration

### wi000 - Slack Integration
- [Alert Notification](https://documentation.wazuh.com/current/user-manual/manager/manual-integration.html#slack)

### wi001 - Sysmon Integration
- [Windows Edpoint](https://documentation.wazuh.com/current/user-manual/manager/wazuh-archives.html#sysmon-integration)
- Linux Endpoint - Pending

### wi002 - YARA Integration
- [Windows/Linux Edpoint](https://documentation.wazuh.com/current/proof-of-concept-guide/detect-malware-yara-integration.html)

## Refences
- [Wazuh Server Administration](https://documentation.wazuh.com/current/user-manual/manager/index.html)
- [Proof of Concept Guide](https://documentation.wazuh.com/current/proof-of-concept-guide/index.html)
- [Wazuh Blog](https://wazuh.com/blog/)
