# **Network-Monitoring**

Network topologies

![Network Topology](/images/381.PNG)

![Network Topology 2](/images/3812.PNG)

# Chatbot Project

## Netmiko Skill - Copy Run Start

### Netmiko skill to copy the running config to the startup config on all three lab routers

- 192.168.122.10
- 192.168.122.20
- 192.168.122.30

Netmiko Code:
```
from netmiko import ConnectHandler
import myNewParamiko as m
import threading

def copyrun_start(router):
    connection = ConnectHandler(**router)
    prompt =  connection.find_prompt()
    if '>' in prompt:
        connection.enable()
    output = connection.save_config()
    print(output)

    print('Closing connection')
    connection.disconnect()
    print('#'*40)

routers = m.get_list_from_file('routers.txt')
threads = list()

for router in routers:
    th = threading.Thread(target=copyrun_start,args=(router,))
    threads.append(th)
   
for th in threads:
    th.start()
for th in threads:
    th.join()
```
Function in 381Bot.py code to run command
```
def netmiko_copyrunstart(incoming_msg):
    """Saving running-config to the startup-config
    """
    response = Response()

    import netmikocopyrun as copyrun
    response.markdown = "Saved running-config to startup-config"
    return response

```
Chatbox commands:

![text](/images/copyrunstart.png)

Operation of bot:

![text](/images/copyrunstart2.png)

## NetConf Skill - Create Loopback1 

### Netconf bot function to create a loopback 1 interface on CSRv1 through Chatbot

```
def netconf_createloopback(incoming_msg):
    """Creating Loopback1 on CSRV1"""
    response = Response()

    import netconf_loopback1 as netconfloop

    response.markdown = "Created Loopback1 on CSRv1"

    return response
```
381bot.py code:

![image](https://user-images.githubusercontent.com/95718746/145130981-74ee17c1-744f-40a4-803b-5bbd84b1fe94.png)

Execution code:

![image](https://user-images.githubusercontent.com/95718746/145131013-9cff7f49-8dc7-4448-998f-9a30ab54cf76.png)

Router 1 loopback creation:

![image](https://user-images.githubusercontent.com/95718746/145131026-0206697c-115d-42cd-8b21-833b03098c01.png)

![image](https://user-images.githubusercontent.com/95718746/145131032-59adda1e-8fed-4df3-9406-4cfdd3a4a2e9.png)

Configuraiton files used:

- [config_templ_ietf_interface.xml](https://github.com/cjschulz1/Network-Monitoring/blob/9336d3df75f46b7cec303703eaa9dadb6564a465/config_templ_ietf_interface.xml)
- [netconf_loopback1.py](https://github.com/cjschulz1/Network-Monitoring/blob/9336d3df75f46b7cec303703eaa9dadb6564a465/netconf_loopback1.py)
- [routersnetconf.py](https://github.com/cjschulz1/Network-Monitoring/blob/9336d3df75f46b7cec303703eaa9dadb6564a465/routersnetconf.py)

## Ansible Skill
### Show ip interface brief on routers 1,2, & 3 with ansible playbook and save to file.

```
def ansible_showipinterfacebrief(incoming_msg):
    """Show ip interface brief on routers 1,2,3
    """
    response = Response()
    import os
    stream = os.popen('ansible-playbook -i ./inventory show_ip_int_br_playbook.yaml')
    output = stream.read()
    output

    response.markdown = "Wrote show ip interface brief to .txt files"
    response.markdown = output
    return response
```

![image](https://user-images.githubusercontent.com/95718746/145132337-4e9c07f7-95bf-4892-8d5b-6d3b3992a530.png)


Files used:
- [ansible.cfg](https://github.com/cjschulz1/Network-Monitoring/blob/d77f98efa4075aea0fd02ef10935268fa396d9c2/ansible.cfg)
- [inventory.txt](https://github.com/cjschulz1/Network-Monitoring/blob/78dc2d52bcbac222bceda248cdadf2c39385f133/inventory)
- [show_ip_int_br_playbook.yaml](https://github.com/cjschulz1/Network-Monitoring/blob/9d28dd9bc17e69f059d02d18ef82a4822f5009ae/show_ip_int_br_playbook.yaml)

Outputs:

![image](https://user-images.githubusercontent.com/95718746/145132134-cc81af74-e1bc-4fb5-8475-5c3451ad4c82.png)

![image](https://user-images.githubusercontent.com/95718746/145132152-be9199fd-657f-4343-8afb-4fa5ca4f9272.png)

![image](https://user-images.githubusercontent.com/95718746/145132165-cf6c3986-d696-4472-9e2d-4487fa0d4212.png)

![image](https://user-images.githubusercontent.com/95718746/145132175-7d4d1b3a-2593-4a9c-8416-2f47bb493e2e.png)

## Genie Robot Skill - Initial Genie Robot

### Chatbot skill to start the initial genie robot script and generate the log files and display the output of the initial snapshot whether it passed or failed. 

```
def genie_robot(incoming_msg):
    """Start Genie Robot Script
    """
    response = Response()
    import os
    stream = os.popen('robot --outputdir robot_initial robot_initial_snapshot.robot')
    output = stream.read()
    output

    response.markdown = "Started Genie Robot Script"
    response.markdown = output
    return response
```


![image](https://user-images.githubusercontent.com/95718746/145132394-917f2f66-de4f-4eb4-ab6b-75587ab41f02.png)


Files used:
- [robot_inital_snapshot.robot](https://github.com/cjschulz1/Network-Monitoring/blob/360c9d75e501bcc0dd966753e4d394a3179c14c3/robot_initial_snapshot.robot)


## Genie Robot Skill - Open Genie Robot Log.html
### Chatbot skill to open the genie robot log.html file in a browser

```
def html_open(incoming_msg):
    """Open the genie log.html file in browser
    """
    response = Response()
    
    import webbrowser
    webbrowser.open_new_tab('file:///home/devasc/labs/devnet-src/sample-app/network_monitor/webex/robot_initial/log.html')

    response.markdown = "Opened log.html in browser"
    return response
```
Bot input:
![image](https://user-images.githubusercontent.com/95718746/145132826-3fd1afd9-cfdd-4bf6-81f3-2e4f7d2d9b9f.png)

Output:

![image](https://user-images.githubusercontent.com/95718746/145132840-84392911-58cd-4794-913c-99e7960e170d.png)

