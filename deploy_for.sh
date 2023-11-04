#!/bin/bash
# This script deploys all Use Cases Configuration for windows/linux endpoint

PKGs=("curl")

for pkg in "${PKGs[@]}"; do
  if dpkg -l | grep -q "^ii  $pkg "; then
    echo -n
  else
    echo -e "Some packages aren't installed\n\tRun $ sudo apt install ${PKGs[@]}"
    exit 1
  fi
done

if [ $# -eq 0 ]; then
  echo -e "Usage:\n\tSelect the platform: \"windows\" or \"linux\" as Parameter\n\tE.g. $ bash deploy_for.sh windows"
  exit 1
fi

D1R="$(dirname $0)"
WzDIR="/var/ossec"

if [ -f "${D1R}/.env" ]; then 
  export $(cat .env | xargs) 
else
  echo -e ".env file for credential not found!"
  exit 1;
fi

if [ $1 == "windows" ]; then
  echo -e "Configuring use cases for windows ..."
  # base config
  cp "${D1R}/windows/w1ndows_s0urces.conf" "${WzDIR}/etc/shared/w1ndows_s0urces/agent.conf"
  cp "${D1R}/windows/config/sysmonconfig.xml" "${WzDIR}/etc/shared/w1ndows_s0urces/sysmonconfig.xml"
  cp "${D1R}/windows/config/osquery.conf" "${WzDIR}/etc/shared/w1ndows_s0urces/osquery.conf"
  # rules file
  cp "${D1R}/windows/abc_w1n_rul3s.xml" "${WzDIR}/etc/rules/abc_w1n_rul3s.xml"
  chmod -R 660 "${WzDIR}/etc/rules/abc_w1n_rul3s.xml"
  chown -R  wazuh:wazuh "${WzDIR}/etc/rules/abc_w1n_rul3s.xml"
  echo -e "Done"
elif [ $1 == "linux" ]; then
  echo -e "Configuring use cases for linux ..."
  # base config
  cp "${D1R}/linux/l1nux_s0urces.conf" "${WzDIR}/etc/shared/l1nux_s0urces/agent.conf"
  # decoder file
  cp "${D1R}/linux/l1nux_d3coders.xml" "${WzDIR}/etc/decoders/l1nux_d3coders.xml"
  chmod -R 660 "${WzDIR}/etc/decoders/l1nux_d3coders.xml"
  chown -R  root:wazuh "${WzDIR}/etc/decoders/l1nux_d3coders.xml"
  # rules file
  cp "${D1R}/linux/abc_l1n_rul3s.xml" "${WzDIR}/etc/rules/abc_l1n_rul3s.xml"
  chmod -R 660 "${WzDIR}/etc/rules/abc_l1n_rul3s.xml"
  chown -R  wazuh:wazuh "${WzDIR}/etc/rules/abc_l1n_rul3s.xml"
  echo -e "Done"
else
  echo -e "Usage:\n\tSelect the platform: \"windows\" or \"linux\" as Parameter\n\tE.g. $ bash deploy_for.sh windows"
fi

# manager conf
sed -i "s|WEBHOOK_URL|${SLACK_HOOK}|g" "${D1R}/manager.conf"
cp "${D1R}/manager.conf"  "${WzDIR}/etc/ossec.conf"
"${WzDIR}/bin/wazuh-control" restart
