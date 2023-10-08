# Wazuh Use Cases for Windows.

## WB0001 - Sysmon integration
*Requirements:*

Install the sysmon to the host to be monitored, manually or via a gpo [sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
We'll use the [Olaf sysmon-modular config](https://wazuh.com/resources/blog/detecting-process-injection-with-wazuh/sysmonconfig.xml) + Wazuh Custom Sysmon Rules

*References:*
- [Sysmon Integration](https://documentation.wazuh.com/current/user-manual/manager/wazuh-archives.html#sysmon-integration)
- [Using Wazuh to monitor Sysmon events](https://wazuh.com/blog/using-wazuh-to-monitor-sysmon-events/)

## Use Cases
### [Hunting for Windows credential access attacks with Wazuh](https://wazuh.com/blog/hunting-for-windows-credential-access-attacks/)
- [Red Team Notes](https://www.ired.team/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz#comsvcs.dll)

## Refences
- [Wazuh Server Administration](https://documentation.wazuh.com/current/user-manual/manager/index.html)
- [Wazuh Blog](https://wazuh.com/blog/)
- [Proof of Concept Guide](https://documentation.wazuh.com/current/proof-of-concept-guide/index.html)

