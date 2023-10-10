# wazuh-usecases-integrator
Wazuh XDR use cases' integrator scripts 

For make changes and command monitoring (remote commands execution) on agent, enable remote_commands for each agents [reference](https://documentation.wazuh.com/current/user-manual/capabilities/command-monitoring/how-it-works.html)
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
