#!/usr/bin/env python3

import subprocess 
import pandas as pd 
from io import StringIO
from colorama import init
from colorama import Fore, Back, Style

def get_raw_connections():
    res = subprocess.check_output(["nmcli","-g","IN-USE,SSID,CHAN,RATE,SIGNAL,BARS,SECURITY","dev","wifi"])
    res = res.decode('utf-8')


    f = StringIO(res)
    prova = pd.read_csv(f, sep=':', header=None) #
    prova.columns = ['CONNECTED','SSID','CHAN','RATE','SIGNAL','BARS','SECURITY']

    prova.index = prova.index + 1
    prova['levels'] = prova['BARS'].apply(lambda x: 4 - x.count('_'))
    prova['levels'] = prova['levels'].map({0: Fore.WHITE, 1: Fore.BLUE, 2: Fore.YELLOW, 3: Fore.GREEN, 4: Fore.GREEN})

    return prova 

def get_default(clean):
    default = clean[clean['CONNECTED'] == '*'].index 
    return default 

def build_menu(clean):
    a_string = clean.iloc[:,:-1].to_string()
    splitted = a_string.split("\n")

    new = []

    for n,s in enumerate(splitted[1:]):
        dim = len(str(n+1))
        new.append(s[:dim] + clean['levels'][n+1] + s[dim:] + Fore.RESET)

    print(splitted[0])
    print("\n".join(new))

def choose_network(clean, default):
    while True:
        number = input(f"\nchoose a network (1-{clean.shape[0]}) [{clean['SSID'][default].to_string()}] >> ")
        try:
            number = int(number)
            break 
        except: 
            print("invalid choise, retry")
            True 
    return clean.loc[number]['SSID']

def password(choosen): 
    password = input(f"insert passphrase for {choosen} >> ")
    return password


if __name__ == '__main__':
    clean = get_raw_connections()
    default = get_default(clean)
    build_menu(clean)
    choosen = choose_network(clean, default)
    password(choosen)