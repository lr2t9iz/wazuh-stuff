@echo off
REM take snapshot
mkdir C:\wazuh_t3mp
netsh advfirewall export "C:\wazuh_t3mp\fw_rules.xml"

REM block all conexion
netsh advfirewall firewall delete rule name=all
netsh advfirewall set allprofile firewallpolicy blockinbound,blockoutbound

REM add exception
netsh advfirewall firewall add rule name="allow-siem-in" dir=in action=allow protocol=any remoteip=10.10.1.2
netsh advfirewall firewall add rule name="allow-siem-out" dir=out action=allow protocol=any remoteip=10.10.1.2
