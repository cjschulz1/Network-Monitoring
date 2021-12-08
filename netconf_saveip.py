from ncclient import manager
import xml.dom.minidom as p
import xmltodict
import routersnetconf

m = manager.connect(**routersnetconf.router)
ip = open("ip.txt").read()
netconf_template = open("config_templ_ietf_interface.xml").read()

netconf_payload = netconf_template.format(int_name="GigabitEthernet",
                                            int_num="2",
                                            int_desc="Configured via netconf through 381Bot",
                                            ip_address=ip,
                                            subnet_mask="255.255.255.0"
                                            )
print("Configuration Payload:")
print("----------------------")
print(netconf_payload)

print('#'*80)

netconf_reply = m.edit_config(target="running", config=netconf_payload)

print(netconf_reply)
