#!/bin/python3

""" 
so this scanner takes input as an ip

"""

import socket,sys
from datetime import datetime



#define a host name 
if len (sys.argv) ==2:
    try:
        target = socket.gethostbyname(sys.argv[1])#transplate the host name


    except Exception as e:
        print("Host cannot be resolved please check target properly ")
        sys.exit()

else :
    print("Please Specify an ip address")
    print(f"Syntax :./Scanner.py <ip> or hostname ")
    sys.exit()


#add a banner
print("-"*50)
start_time = str(datetime.now().strftime("%H:%M:%S"))
print("Scanning target {}".format(target))
print(f"Time started: {start_time}")
print("-"*50)



try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))

        if result ==0:
            print("Port {} is open".format(port))
        s.close()



except KeyboardInterrupt:
    print("\nOh no........")
    print("Exiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname cannot be resolved. ")
    sys.exit()

except socket.error:
    print("Couldn't connect to host")
    sys.exit()


end_time =str(datetime.now().strftime("%H:%M:%S"))
print(f"Time taken: {end_time}")