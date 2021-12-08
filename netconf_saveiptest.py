from ncclient import manager
import xml.dom.minidom as p
import xmltodict
import routersnetconf

m = manager.connect(**routersnetconf.router)
ip = open("ip.txt").read()
netconf_template = open("config_templ_ietf_interfacetest.xml").read()

netconf_payload = netconf_template.format(ip_address=ip)
                                            
print("Configuration Payload:")
print("----------------------")
print(netconf_payload)

print('#'*80)

netconf_reply = m.edit_config(target="running", config=netconf_payload)

print(netconf_reply)
