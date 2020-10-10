#!/usr/bin/env python3

import re 
import subprocess 
import pandas as pd 
from io import StringIO
from colorama import init
from colorama import Fore, Back, Style

init()

pd.set_option('display.width',None)
pd.set_option('expand_frame_repr', False)
pd.set_option("display.max_rows", None, "display.max_columns", None)

res = subprocess.check_output(["nmcli","-g","IN-USE,SSID,CHAN,RATE,SIGNAL,BARS,SECURITY","dev","wifi"])
res = res.decode('utf-8')


f = StringIO(res)
prova = pd.read_csv(f, sep=':', header=None) #
prova.columns = ['CONNECTED','SSID','CHAN','RATE','SIGNAL','BARS','SECURITY']

prova.index = prova.index + 1
prova['levels'] = prova['BARS'].apply(lambda x: 4 - x.count('_'))
prova['levels'] = prova['levels'].map({1: Fore.BLUE, 2: Fore.YELLOW, 3: Fore.GREEN, 4: Fore.GREEN})

size = prova.shape[0]

a_string = prova.iloc[:,:-1].to_string()
splitted = a_string.split("\n")

new = []

for n,s in enumerate(splitted[1:]):
    dim = len(str(n+1))
    #print(prova['levels'][n+1])
    new.append(s[:dim] + prova['levels'][n+1] + s[dim:] + Fore.RESET)

print(splitted[0])
print("\n".join(new))