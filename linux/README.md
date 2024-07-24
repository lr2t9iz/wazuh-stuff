# Wazuh Use Cases for Linux

## Requirements
- Enable remote command execution on Wazuh agents 
```sh
# https://documentation.wazuh.com/current/user-manual/capabilities/command-monitoring/configuration.html#example-configuration
echo 'logcollector.remote_commands=1' >> /var/ossec/etc/local_internal_options.conf

systemctl restart wazuh-agent
```

## Use Cases
### uc0001 [Malware Detection with FIM and YARA](https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/fim-yara.html)
- MITRE ATT&CK Refereces
- Attacks Simulation/Emulation
