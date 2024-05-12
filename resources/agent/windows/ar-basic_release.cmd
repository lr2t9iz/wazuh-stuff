@echo off
REM rollback 
netsh advfirewall import "C:\wazuh_t3mp\fw_rules.xml"

REM clear
rmdir C:\wazuh_t3mp
