# **Network Monitoring ChatBox Project by Colin & Connor Schulz**

Configure the network topology as follows:

![Network Topology](/images/381.PNG)

![Network Topology 2](/images/3812.PNG)




# Chatbot Project

## Netmiko Skill - Copy Run Start

### Netmiko skill to copy the running config to the startup config on all three lab routers

- 192.168.122.10
- 192.168.122.20
- 192.168.122.30

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
Files Used:
- [netmikocopyrun.py](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/netmikocopyrun.py)

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

- [config_templ_ietf_interface.xml](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/config_templ_ietf_interface.xml)
- [netconf_loopback1.py](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/netconf_loopback1.py)
- [routersnetconf.py](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/routersnetconf.py)

## Ansible Skill
### Show ip interface brief on routers 1,2, & 3 with ansible playbook and save to file.

```
def ansible_showipinterfacebrief(incoming_msg):
    """Show ip interface brief on routers 1,2,3"""
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
- [ansible.cfg](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/ansible.cfg)
- [inventory.txt](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/inventory)
- [show_ip_int_br_playbook.yaml](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/show_ip_int_br_playbook.yaml)

Outputs:

![image](https://user-images.githubusercontent.com/95718746/145132134-cc81af74-e1bc-4fb5-8475-5c3451ad4c82.png)

![image](https://user-images.githubusercontent.com/95718746/145132152-be9199fd-657f-4343-8afb-4fa5ca4f9272.png)

![image](https://user-images.githubusercontent.com/95718746/145132165-cf6c3986-d696-4472-9e2d-4487fa0d4212.png)

![image](https://user-images.githubusercontent.com/95718746/145132175-7d4d1b3a-2593-4a9c-8416-2f47bb493e2e.png)

## Genie Robot Skill - Initial Genie Robot

### Chatbot skill to start the initial genie robot script and generate the log files and display the output of the initial snapshot whether it passed or failed. 

```
def genie_robot(incoming_msg):
    """Start Genie Robot Script"""
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
- [robot_inital_snapshot.robot](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/robot_initial_snapshot.robot)


## Genie Robot Skill - Open Genie Robot Log.html
### Chatbot skill to open the genie robot log.html file in a browser

```
def html_open(incoming_msg):
    """Open the genie log.html file in browser"""
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


## Genie Robot Skill - Compare & Open Genie Robot Log.html
### Chatbot skill to run the compare script and then open the compare log.htm with Shutdown G2 interface

```
def genie_robot_compare(incoming_msg):
    """Compare Genie Robot Script"""
    response = Response()
    import os
    stream = os.popen('robot --outputdir robot_compare robot_compare_snapshot.robot')
    output = stream.read()
    output

    import webbrowser
    webbrowser.open_new_tab('file:///home/devasc/labs/devnet-src/sample-app/network_monitor/webex/robot_compare/log.html')

    response.markdown = "Opened log.html Genie Robot Compare Script"
    response.markdown = output
    return response
```

File Used:
- [robot_compare_snapshot.robot](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/robot_compare_snapshot.robot)


Robot Input:

![image](https://user-images.githubusercontent.com/95718746/145133283-55fad78c-454e-4671-82b3-4f1c9263af40.png)

![image](https://user-images.githubusercontent.com/95718746/145133302-9415fe31-f775-4e4c-ab39-87b9afe975db.png)

Log File:

![image](https://user-images.githubusercontent.com/95718746/145133325-a150dae3-3c17-44a8-b0b0-7ee43f8dc9e2.png)


## Genie Monitor for Disaster Skill - Genie Disaster Initial Part 1

### Initialize the genie robot to then later compare for changes

```
def genie_disaster_initial(incoming_msg):
    """Set up inital genie snapshot"""
    response = Response()
    
    import os
    stream = os.popen('robot --outputdir robot_initial robot_initial_snapshot.robot')
    output = stream.read()
    output

    import webbrowser
    webbrowser.open_new_tab('file:///home/devasc/labs/devnet-src/sample-app/network_monitor/webex/robot_initial/log.html')

    response.markdown = "Created snapshot as log.html"
    return response
```

Robot Input:

![image](https://user-images.githubusercontent.com/95718746/145133585-b94044bd-2d94-4646-9183-80511eba992c.png)

Log:

![image](https://user-images.githubusercontent.com/95718746/145133608-d669cf9b-de3b-46c1-8f97-6c88abb6409e.png)



## Genie Monitor for Disaster Skill - Genie Disaster Compare Part 2

### Genie robot compare for interface change and open log.html, GigabitEthernet 2 changed to 172.16.0.3 on CSR2

```
def genie_disaster_compare(incoming_msg):
    """Compare Genie Robot Script with initial snapshot to see if ip address changed and update it"""
    response = Response()
    import os
    stream = os.popen('robot --outputdir robot_compare robot_compare_snapshot.robot')
    output = stream.read()
    output

    import webbrowser
    webbrowser.open_new_tab('file:///home/devasc/labs/devnet-src/sample-app/network_monitor/webex/robot_compare/log.html')

    response.markdown = "Opened log.html Genie Robot Compare Script"
    response.markdown = output
    return response
```

Input:

![image](https://user-images.githubusercontent.com/95718746/145133747-a37561bf-d839-4907-909e-c44772ef9351.png)


Output:

![image](https://user-images.githubusercontent.com/95718746/145133757-96c4cd3f-63f6-4960-b97f-aaeee7a1a3bc.png)



## Genie Monitor for Disaster Skill - Netconf save new IP Part 3
### Netconf script to save new ip address from text file ip.txt entered by user into GigabitEthernet2 automatically.

```
def genie_disaster_saveip(incoming_msg):
    """Save new ip to text file
    """
    response = Response()

    val = input("Enter your new ip: ")

    with open("ip.txt", "w") as text_file:
        text_file.write(val)

    import netconf_saveip as saveip
    import netconf_saveiptest as saveiptest
    response.markdown = "Updated IP address of GigabitEthernet2"
    return response
```

Files used:

- [netconf_saveiptest.py](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/netconf_saveiptest.py)

Input:

![image](https://user-images.githubusercontent.com/95718746/145134037-3b184633-3ea3-453e-86d5-0dec63c7dedc.png)

Output:

![image](https://user-images.githubusercontent.com/95718746/145134070-f55b6c6a-77a2-49fc-9f60-73bd048eab84.png)

Enter New IP address in python CLI ^

![image](https://user-images.githubusercontent.com/95718746/145134086-ea9cf256-9075-4aed-840d-4f2a43c9f7cf.png)


## Genie Monitor for Disaster Skill - Genie Disaster Netconf update VPN IP Part 4
### Netconf script update the new ip in VPN connection on HQ/CSR1 as well

```
def genie_disaster_saveip(incoming_msg):
    """Save new ip to text file
    """
    response = Response()

    val = input("Enter your new ip: ")

    with open("ip.txt", "w") as text_file:
        text_file.write(val)

    import netconf_saveip as saveip
    import netconf_saveiptest as saveiptest
    response.markdown = "Updated IP address of GigabitEthernet2 and CSR1 VPN"
    return response
```

Files Used:
- [netconf_saveiptest.py](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/netconf_saveiptest.py)
- [config_templ_ietf_interfacetest.xml](https://github.com/cjschulz1/Network-Monitoring/blob/dffabf0aeee61863746437fd7b0af76e5ba4a591/file/config_templ_ietf_interfacetest.xml)


Output:

![image](https://user-images.githubusercontent.com/95718746/145134899-44f11ee7-2997-4d0a-966d-e452b024587f.png)


















