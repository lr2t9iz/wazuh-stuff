# Wazuh Use Cases for Windows.

## Requirements 
- Enable powershell logging
```PowerShell
# https://c-137lab.com/posts/powershell_logg1ng/
$basePath = "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging"
if (-not (Test-Path $basePath)) { $null = New-Item $basePath -Force }
Set-ItemProperty $basePath -Name EnableScriptBlockLogging -Value "1"
```
- Enable TaskScheduler logs
```PowerShell
# https://c-137lab.com/posts/scheduled_t4sk/
wevtutil sl Microsoft-Windows-TaskScheduler/Operational /enabled:true
```
- Install Sysmon
```PowerShell
# https://c-137lab.com/posts/sysm0n/
.\Sysmon64.exe -accepteula -i sysmonconfig.xml
```

## Use Cases
### uc00001 [Hunting for Windows credential access attacks with Sysmon](https://wazuh.com/blog/hunting-for-windows-credential-access-attacks/)
- MITRE ATT&CK Refereces
  - [OS Credential Dumping](https://attack.mitre.org/techniques/T1003/)
- Attacks Simulation/Emulation
  - [Atomic Red Team](https://atomicredteam.io/credential-access/T1003/)
  - [Red Team Notes](https://www.ired.team/offensive-security/credential-access-and-credential-dumping/)

### uc00002 Chrome extension accounted with Osquery
- MITRE ATT&CK References
  - [Browser Extensions](https://attack.mitre.org/techniques/T1176/)
- Attacks Simulation/Emulation
  - Install/remove an Chrome extension
