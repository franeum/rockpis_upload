#!/usr/bin/env python3

import subprocess 

def get_raw_connections():
    result = subprocess.check_output(["nmcli","-f","IN-USE,SSID","dev","wifi"])
    result = result.decode('utf-8')
    result = result.split('\n')[1:-1]
    return result 

def clean_result(result):
    clean = []
    for x in result:
        s = x.strip(None)
        if s[0] == '*':
            clean.append((s[1:].strip(None),1))
        else:
            clean.append((s,0))
    return clean 

def get_default(clean):
    default = filter(lambda x: x[1] == 1, clean)
    default = list(default)[0][0]
    return default 

def build_menu(clean):
    for n, x in enumerate(clean):
        if x[1] == 1:
            print(f"{n+1}.\t{x[0]}\t(*)")
        else:
            print(f"{n+1}.\t{x[0]}")

def choose_network(clean, default):
    while True:
        number = input(f"\nchoose a network (1-{len(clean)}) (default: {default}) >> ")
        try:
            number = int(number)
            break 
        except: 
            print("invalid choise, retry")
            True 
    return clean[number-1][0]

def password(choosen): 
    password = input(f"insert passphrase for {choosen} > ")
    return password


if __name__ == '__main__':
    result = get_raw_connections()
    clean = clean_result(result)
    default = get_default(clean)
    build_menu(clean)
    choosen = choose_network(clean, default)
    password(choosen)
    "▂▄▆█_"