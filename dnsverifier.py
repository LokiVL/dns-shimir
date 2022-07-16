import os
from statistics import mean
from ping3 import ping

# Class used to manage each DNS info
class DnsPing:
    def __init__(self, ip, mean_resp):
        self.ip = ip
        self.mean_resp = mean_resp

# Verify if dns.txt exists
if os.path.exists("dns.txt"):

    # Get all DNS
    with open("dns.txt", "r") as dns_file:
        dns_list = []
        for line in dns_file.readlines():

            # Just get lines with DNS IPs
            if len(line) > 1 and line.find("#") == -1:
                dns_list.append(line)
        dns_file.close()

    # Verify if DNS list has DNS IP on it
    if len(dns_list) < 1:
        print("DNS List is empty, please verify 'dns.txt' file.")
        quit()

    dns_ping_ms = [] # List to storage DNS info

    # Ping each DNS 10 times and get its mean response
    for dns in dns_list:        
        pings = []
        
        for cont in range (10):
            ping_ =  ping(dns.strip("\n"))
            if ping_ != None and ping_ != False: # Treatment for Timeout   
                pings.append(ping_ * 1000)
            else:
                print("IP: {} || Fail".format(dns.strip("\n")))
                break
        
        if len(pings) == 10:
            dns_ = DnsPing(dns.strip("\n"), mean(pings)) # Saving info in a object
            dns_ping_ms.append(dns_) # Saving object for future sort

            print("IP: {} || {:.0f} ms".format(dns.strip("\n"), mean(pings)))
            for cont in range(len(pings)):
                print("     Ping{}: {:.0f} ms".format(cont+1, pings[cont]))
    
    dns_ping_ms.sort(key=lambda x: x.mean_resp) # Sorting DNS mean response list by lowest to highest

    # Printing the 5 fastest DNS
    for cont in range(5):
        print("{}º - {} ({:.0f} ms)".format(cont + 1, dns_ping_ms[cont].ip, dns_ping_ms[cont].mean_resp))

# Treatment for "dns.txt" not found
else:
    print("'dns.txt' couldn't be found. Creating...")

    tries = 0
    while not os.path.exists("dns.txt"):

        # Creating tries
        if tries == 5:
            print("A problem occurred during 'dns.txt' creation. Please restart tool.")
            quit()

        with open("dns.txt", "x") as dns_file:
            dns_file.close()
        
        tries = tries + 1

    print("'dns.txt' created! Please, fill it and restart tool.")