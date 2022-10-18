from netmiko import ConnectHandler

with open('device_ips.txt') as devs:
    for ip in devs:
        dev = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'username', #replace with relevant creds
            'password': 'password' #replace with relevant creds
        }
    
    networkConnection = ConnectHandler(**dev)
    host = networkConnection.send_command('show run | i host')
    host.split(" ")
    host,device = host.split(" ")
    print('Running config backup for device: ' + device)

    #dumps to working dir
    saveFile = device + '.txt'

    #dumps to specific dir (comment out above line, uncomment and modify below)
    #saveFile = '/home/matt/ios_backups/' + device + '.txt'

    showrun = networkConnection.send_command('show run')
    showVlan = networkConnection.send_command('show vlan')
    showVer = networkConnection.send_command('show ver')

    logFile = open(saveFile, 'a')
    logFile.write(showrun + '\n' + showVlan + '\n' + showVer + '\n')

networkConnection.disconnect()