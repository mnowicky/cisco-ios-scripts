from netmiko import ConnectHandler
import getpass

def issueCommands():
    u = input('Enter username: ')
    p = getpass.getpass('Enter pw: ')
    routeTarget = input('Checking routes to target device?\n' '(Y/n)')
    if(routeTarget == 'Y'):
        routeTargetIP = input('Enter IP of target device for routing outputs:\n')


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

        ver = connection.send_command('show ver')

        interfaces = connection.send_command('show ip int brief')
        vlans = connection.send_command('show vlan brief')
        routes = connection.send_command('show ip route')
        accLog = connection.send_command('show vlan access-log config')
        spanningTree = connection.send_command('show spanning-tree')
        if(routeTarget and routeTargetIP):
            rTarget = connection.send_command('show ip route' + routeTargetIP)

        saveFile = dev.host + '_reportInfo' + '.txt'
        logFile = open(saveFile, 'a')
        logFile.write(interfaces + '\n' + vlans + '\n' + routes + '\n' + accLog + '\n' + spanningTree + '\n')
        if(rTarget):
            logFile.write(rTarget+'\n')
        
        print(interfaces + '\n' + vlans + '\n' + routes + '\n' + accLog + '\n' + spanningTree + '\n')
        if(rTarget):
            print(rTarget+'\n')

    connection.disconnect()

if(__name__ == "main"):
    issueCommands()