# Wazuh Use Cases for Linux

## wi002 - FIM Integration

## wi003 - YARA Integration
**Requirements:** Compile and install yara binaries on the host to be monitored, manually or via gpo [yara](https://yara.readthedocs.io/en/stable/gettingstarted.html).
- Copy `./linux/ar-script/<scripts>` in `/var/ossec/active-response/bin/` on the endpoint [Custom Script](https://documentation.wazuh.com/current/user-manual/capabilities/active-response/custom-active-response-scripts.html#linux-unix-custom-active-response-configuration)
- Install the `jq` on the endpoint


## Use Cases
### uc0002 [File integrity monitoring and YARA](https://documentation.wazuh.com/current/user-manual/capabilities/malware-detection/fim-yara.html)
- 
