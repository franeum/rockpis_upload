#!/usr/bin/env python3

import subprocess 

result = subprocess.check_output(["nmcli","-f","IN-USE,SSID","dev","wifi"])
result = result.decode('utf-8')

result = result.split('\n')[1:-1]
cleaned = []

for x in result:
    s = x.strip(None)
    if s[0] == '*':
        cleaned.append((s[1:].strip(None),1))
    else:
        cleaned.append((s,0))

default = filter(lambda x: x[1] == 1, cleaned)
default = list(default)[0][0]

for n, x in enumerate(result):
    print(f"{n+1}.\t{x}")

while True:
    number = input(f"\nchoose a network (1-{len(result)}) (default: {default}) > ")
    try:
        number = int(number)
        break 
    except: 
        True 
choosen = cleaned[number-1][0]
password = input(f"insert passphrase for {choosen} > ")