from netmiko import ConnectHandler
import getpass

def issueCommands():
    u = input('Enter username: ')
    p = getpass.getpass('Enter pw: ')

    with open('device_ips.txt') as devs:
        for ip in devs:
            dev = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': u,
                'password': p, 
                'secret': p #enable pw
            }
        
        connection = ConnectHandler(**dev)
        connection.enable()

        #Sample commands config, replace with whatever you need
        #commands = ['interface gi0/0', 'descri WAN', 'exit', 'access-list 1 permit any']
        commands = ['reload', 'Y', '\n']
        connection.send_config_set(commands)

    connection.disconnect()

if(__name__ == "main"):
    issueCommands()