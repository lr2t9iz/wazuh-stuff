# External API integration
- https://documentation.wazuh.com/current/user-manual/manager/integration-with-external-apis.html

- requirements
```sh
/var/ossec/framework/python/bin/pip3 install --upgrade pip
/var/ossec/framework/python/bin/pip3 install requests python-dotenv
```

## Wazuh XDR Enhanced Module (Python-based)
- **correlation/** contains rule modules designed to correlate collected logs (wazuh alerts) in search of potential threats.
- **response/** contains action modules that define what to do in case of a potential threat.
- **utils/** contains connections to databases, APIs, and similar resources.
- **custom-xdr** file orchestrates the correlation and response modules, dynamically executing them to manage detection and response workflows.