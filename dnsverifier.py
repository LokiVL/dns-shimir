from tools.verification import *
from tools.util import *

# Class used to manage each DNS info
class DnsPing:
    def __init__(self, ip, mean_resp):
        self.ip = ip
        self.mean_resp = mean_resp

op = 1
while op != 0:
    printTitle("DNS SHIMIR")
    print("1 - Local Verification (Verification is done based on your location)")
    print("2 - Custom Verification (You choose which DNS IPs will be verified)")
    print("\n0 - Exit")
    op = int(input("\nEnter verification you want: "))

    if op == 0:
        exit()
    elif op == 1:
        dns_list = localVerification()
        break
    elif op == 2:
        dns_list = customVerification()
        break
    else:
        print("Invalid option.")
    clearScreen()

if type(dns_list) == list:
    clearScreen()
    exec_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Storage execution date
    exec_time_start = datetime.now().replace(microsecond=0) # Storage start time

    dns_ping_ms = [] # List to storage DNS info
    dns_ping_fail = [] # List to storage failed Pings

    # Ping each DNS 10 times and get its mean response
    for dns in tqdm(dns_list):
        pings = []
        
        for cont in range (10):
            ping_ =  ping(dns.strip("\n"))
            if ping_ != None and ping_ != False: # Treatment for Timeout   
                pings.append(ping_ * 1000)
            else:
                dns_ping_fail.append(dns.strip("\n"))
                break
        
        if len(pings) == 10:
            dns_ = DnsPing(dns.strip("\n"), mean(pings)) # Saving info in a object
            dns_ping_ms.append(dns_) # Saving object for future sort

    exec_time_finish = datetime.now().replace(microsecond=0) # Storage finish time

    clearScreen()
    # Printing execution information
    printTitle("EXECUTION INFORMATION")
    print("Date: {}".format(exec_date))
    print("Duration: {}".format((exec_time_finish - exec_time_start)))

    # Printing the 5 fastest DNS
    printTitle("FASTEST PING RESULTS")

    dns_ping_ms.sort(key=lambda x: x.mean_resp) # Sorting DNS mean response list by lowest to highest
    for cont in range(len(dns_ping_ms)):
        print("{}º - {} ({:.0f} ms)".format(cont + 1, dns_ping_ms[cont].ip, dns_ping_ms[cont].mean_resp))
        
        if cont == 4:
            break

    # Printing DNS with Fail Pings
    if len(dns_ping_fail) > 0:
        printTitle("FAIL PINGS")

        print(dns_ping_fail[0], end="")

        for dns in dns_ping_fail:
            if dns != dns_ping_fail[0]:
                print(", " + dns, end="")
        print("") # Breakline

    # Printing remaining Ping results
    if len(dns_ping_ms) > 5: 
        printTitle("OTHER PING RESULTS")
        print("{} ({:.0f} ms)".format(dns_ping_ms[5].ip, dns_ping_ms[5].mean_resp), end="")

        for dns in dns_ping_ms:
            if dns != dns_ping_ms[0] and dns != dns_ping_ms[1] and dns != dns_ping_ms[2] and dns != dns_ping_ms[3] and dns != dns_ping_ms[4] and dns != dns_ping_ms[5]:
                print(", {} ({:.0f} ms)".format(dns.ip, dns.mean_resp), end="")
input("")