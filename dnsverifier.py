import os
from datetime import datetime
from statistics import mean
from ping3 import ping

# Class used to manage each DNS info
class DnsPing:
    def __init__(self, ip, mean_resp):
        self.ip = ip
        self.mean_resp = mean_resp

# Verify if dns.txt exists
if os.path.exists("dns.txt"):

    exec_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Storage execution date
    exec_time_start = datetime.now().replace(microsecond=0) # Storage start time

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
    dns_ping_fail = [] # List to storage failed Pings

    # Ping each DNS 10 times and get its mean response
    for dns in dns_list:        
        pings = []
        
        for cont in range (10):
            ping_ =  ping(dns.strip("\n"))
            if ping_ != None and ping_ != False: # Treatment for Timeout   
                pings.append(ping_ * 1000)
            else:
                print("IP: {} || Fail".format(dns.strip("\n")))
                dns_ping_fail.append(dns.strip("\n"))
                break
        
        if len(pings) == 10:
            dns_ = DnsPing(dns.strip("\n"), mean(pings)) # Saving info in a object
            dns_ping_ms.append(dns_) # Saving object for future sort

            print("IP: {} || {:.0f} ms".format(dns.strip("\n"), mean(pings)))
            for cont in range(len(pings)):
                print("     Ping{}: {:.0f} ms".format(cont+1, pings[cont]))
    
    exec_time_finish = datetime.now().replace(microsecond=0) # Storage finish time

    # Printing execution information
    print("\n====== EXECUTION INFORMATION ======\n")
    print("Date: {}".format(exec_date))
    print("Duration: {}".format((exec_time_finish - exec_time_start)))

    # Printing the 5 fastest DNS
    print("\n====== FASTEST PING RESULTS ======\n")
    
    dns_ping_ms.sort(key=lambda x: x.mean_resp) # Sorting DNS mean response list by lowest to highest
    for cont in range(len(dns_ping_ms)):
        print("{}º - {} ({:.0f} ms)".format(cont + 1, dns_ping_ms[cont].ip, dns_ping_ms[cont].mean_resp))
        
        if cont == 4:
            break
    
    # Printing DNS with Fail Pings
    if len(dns_ping_fail) > 0:
        print("\n====== FAIL PINGS ======\n")

        print(dns_ping_fail[0], end="")

        for dns in dns_ping_fail:
            if dns != dns_ping_fail[0]:
                print(", " + dns, end="")
        print("") # Breakline

    # Printing remaining Ping results
    if len(dns_ping_ms) > 5: 
        print("\n====== OTHER PING RESULTS ======\n")    
        print("{} ({:.0f} ms)".format(dns_ping_ms[5].ip, dns_ping_ms[5].mean_resp), end="")

        for dns in dns_ping_ms:
            if dns != dns_ping_ms[0] and dns != dns_ping_ms[1] and dns != dns_ping_ms[2] and dns != dns_ping_ms[3] and dns != dns_ping_ms[4] and dns != dns_ping_ms[5]:
                print(", {} ({:.0f} ms)".format(dns.ip, dns.mean_resp), end="")
    
# Treatment for "dns.txt" not found
else:
    print("'dns.txt' couldn't be found. Creating...")

    tries = 0
    while not os.path.exists("dns.txt"):

        with open("dns.txt", "x") as dns_file:
            dns_file.close()

        # Verify creation tries
        if tries == 5:
            print("A problem occurred during 'dns.txt' creation. Please restart tool.")
            quit()        
        tries = tries + 1

    print("'dns.txt' created! Please, fill it and restart tool.")