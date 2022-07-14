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
        dns_list = dns_file.readlines()
        dns_file.close()

    dns_ping_ms = []

    # Ping each DNS 10 times and get its mean response
    for dns in dns_list:        
        pings = []

        if ping(dns.strip("\n")) != None and ping(dns.strip("\n")) != False: # Treatment for Timeout
            for cont in range (10):            
                pings.append(ping(dns.strip("\n")) * 1000)
            
            dns_ = DnsPing(dns.strip("\n"), mean(pings)) # Saving info in a object

            dns_ping_ms.append(dns_) # Saving object for future sort

        '''print("IP: {} || {:.0f} ms".format(dns.strip("\n"), mean(pings)))
        for cont in range(len(pings)):
            print("     Ping{}: {:.0f} ms".format(cont+1, pings[cont]))'''
    
    dns_ping_ms.sort(key=lambda x: x.mean_resp) # Sorting DNS mean response list by lowest to highest
    for cont in range(5):
        print("{}º - {} ({:.0f} ms)".format(cont + 1, dns_ping_ms[cont].ip, dns_ping_ms[cont].mean_resp))