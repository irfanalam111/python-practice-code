import nmap
scanner=nmap.PortScanner()
ip_add=input("Enter the IP address: ")
respo=input('''\n Please Enter Your Type Of Scan You Want to run
               1) SYN ACK Scan
               2) UDP Scan
               3) Comprehesive Scan
               4) Regular Scan
               5) OS Detection 
               6) Multiple IP inputs
               7) Ping Scan\n''')
print("you have selected option: ",respo)

if respo == 1:
   print("Nmap Version: ",scanner.nmap_version())
   scanner.scan(ip_add,'1-1024','-v -sS')
   print(scanner.scaninfo())
   print("Ip Status: ",scanner[ip_add].state())
   print("protocols: ",scanner[ip_add].all_protocols())
   print("open Ports: ",scanner[ip_add]['tcp'].keys())

elif respo ==2:
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_add, '1-1024','-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_add].state())
    print("Protocols: ",scanner[ip_add].all_protocols())
    print("Open Ports: ",scanner[ip_add]['udp'].keys())
elif respo ==3:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_add].state())
    print("Protocols: ", scanner[ip_add].all_protocols())
    print("Open Ports: ", scanner[ip_add]['udp'].keys())
elif respo ==4:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_add)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_add].state())
    print("Protocols: ", scanner[ip_add].all_protocols())
    print("Open Ports: ", scanner[ip_add]['tcp'].keys())
elif respo ==5:
    print(scanner.scan(ip_add,arguments="-O")['scan'][ip_add]['osmatch'][1])
elif respo ==6:
    ip_add = input()
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_add,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ",scanner[ip_add].state())
    print("porotocol: ",scanner[ip_add].all_protocols())
    print("open Ports: ",scanner[ip_add]['tcp'].keys())
elif respo ==7:
       scanner.scan(hosts='192.168.1.0/24',arguments='-n -sP -PE -PA21,23,80,3389')
       hosts_list=[(X,scanner[X]['status']['state']) for X in  scanner.all_hosts() ]
       for host,status in hosts_list:
           print('{0}:{1}'.format(host,status))
else:
           print("please choose a number from the options above")
