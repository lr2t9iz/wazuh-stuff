D1R="$(dirname $0)"
WzDIR="/var/ossec"
rule_files=("aaa_w1n_overwrite.xml" "abc_w1n_base.xml")

# Update changes
for r_file in ${rule_files[@]}; do
  cp "${D1R}/windows/detection-rules/$r_file" "${WzDIR}/etc/rules/$r_file"
  chmod -R 660 "${WzDIR}/etc/rules/$r_file"
  chown -R  wazuh:wazuh "${WzDIR}/etc/rules/$r_file"
done

# Apply changes
"${WzDIR}/bin/wazuh-control" restart