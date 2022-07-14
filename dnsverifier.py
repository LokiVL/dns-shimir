from msilib.schema import Media
import os
from statistics import mean, median
from ping3 import ping
import math

if os.path.exists("dns.txt"):
    with open("dns.txt", "r") as dns_file:
        dns_list = dns_file.readlines()
        dns_file.close()
    for dns in dns_list:
        pings = []
        for cont in range (10):
            pings.append(ping(dns.strip("\n")) * 1000)
        
        print("IP: {} || {:.0f} ms".format(dns.strip("\n"), mean(pings)))
        for cont in range(len(pings)):
            print("     Ping{}: {:.0f} ms".format(cont+1, pings[cont]))