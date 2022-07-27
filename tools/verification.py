import os

'''
This file was created to storage functions related to 
manipulate DNS IPs used during dns-shimir's execution
and decide how it'll be used.
'''

def customVerification():

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
        return dns_list

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

def localVerification():
    return "localVerification"

