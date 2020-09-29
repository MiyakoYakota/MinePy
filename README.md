# MinePy
A Cross-Platform Minecraft Checker - Designed for Online Shops

## What is this?
This is a tool used for checking Minecraft accounts and checking if they work.

## Should I use this for Cracking Accounts?
Maybe. It's lacking some pretty common features, Namely: 
- ~~Multi-Threading~~ (Added with new update)
- A Fancy UI

## Okay, if I shouldn't use this who should?
If you're someone like myself that has some servers in the sky running linux, you'll find that it's hard to find checking tools that support them. Say if you're running a Shoppify/Selly to sell Minecraft accounts. You can use this tool to check your inventory to make sure that all the accounts are working and up to date. Both services have well documented APIs that can intergrate with this easily.

## How to use this?
Make a file called `combos.txt` and place all your accounts in `email:password` format.

Make another file called `proxies.txt` and place all your proxies in `IP:Port` format.

Run `pip install -r requirements.txt`

Start it with `python MinePy.py`

And specify the amount of threads you'd like to use.
