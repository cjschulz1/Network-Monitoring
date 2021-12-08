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

