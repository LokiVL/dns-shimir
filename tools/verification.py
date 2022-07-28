from tools.util import *

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
    clearScreen()

    # Class to storage country information
    class Country:
        def __init__(self, name, path):
            self.name = name
            self.path = path
        def __repr__(self):
            return "(" + self.name + ", " + self.path + ")"

    # Do a request to public-dns to get html source code
    public_dns_req = BeautifulSoup(requests.get("https://public-dns.info/").text, "html.parser")
    country_list = []

    # Storage available countries in a list
    for link in public_dns_req.find_all("a"):
        if str(link).find("/nameserver/") != -1:
            country_list.append(Country(str(link.contents).strip("'[]"), str(link.attrs)[10:].strip("'}")))

    # Show menu to select country
    printTitle("LOCAL VERIFICATION")
    print("Where are you from?\n")    
    for country in country_list:
        print(str(country_list.index(country)) + " - " + country.name)
    country_op = int(input("\nEnter the correspoding country number: "))

    while country_op < 0 or country_op > (len(country_list) - 1):
        country_op = int(input("Invalid Option. Enter the correspoding country number: "))

    print("\nSelected country: {}".format(country_list[country_op].name))