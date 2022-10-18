device_ips.txt:
a list of Cisco IOS routers or switches to be referenced by scripts, list IPv4 addr of each router. 

backup-routers.py:
Saves running-config of all devices in devices.txt to local dir. 
Move comments in script to save to target dir.

pingTrace.py:
Issues health checks (pings n' traceroutes) for devices listed in device_ips.txt

issueCommands.py:
Issues custom commands to all devices in devices.txt; useful for reloading, multiple config changes, etc. 

troubleShootReport.py:
Displays and logs a decent amount of information regarding interfaces, vlans, routes, and accepts input to display specific routes to target device. 
Modify as needed with your own output you would like included. 