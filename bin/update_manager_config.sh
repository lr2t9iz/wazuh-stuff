D1R="$(dirname $0)/.."
WzDIR="/var/ossec"

if [ -f "${D1R}/.env" ]; then 
  export $(cat ${D1R}/.env | xargs) 
else
  echo -e ".env file for credential not found!"
  exit 1;
fi

cp "${D1R}/resources/manager/default_group.xml" "${WzDIR}/etc/shared/default/agent.conf"

# edit manager config <- creds
sed -i "s|SLACK_HOOK|${SLACK_HOOK}|g" "${D1R}/resources/manager/manager.xml"
# sed -i "s|TEAMS_HOOK|${TEAMS_HOOK}|g" "${D1R}/resources/manager/manager.xml"

cp "${D1R}/resources/manager/manager.xml"  "${WzDIR}/etc/ossec.conf"
"${WzDIR}/bin/wazuh-control" restart