# WAZUH - Use Cases Integrator [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/mit/)

## Overview

Wazuh XDR use cases' integrator scripts 

## Prerequisites
- Have Wazuh Installed [Installation Guide](https://documentation.wazuh.com/current/deployment-options/index.html) or [Wazuh Docker Bundle](https://github.com/lr2t9iz/wazuh-docker-bundle)

- Creation of groups on Wazuh Dashobard
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

## Refences
- [Wazuh Server Administration](https://documentation.wazuh.com/current/user-manual/manager/index.html)
- [Proof of Concept Guide](https://documentation.wazuh.com/current/proof-of-concept-guide/index.html)
- [Wazuh Blog](https://wazuh.com/blog/)
