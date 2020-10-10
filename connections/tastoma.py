#!/usr/bin/env python3

import re 
import subprocess 
import pandas as pd 

pattern = re.compile(r"(\*?\s+) (.+\s?) ([▂▄▆█_]+) ([0-9]+)")
res = subprocess.check_output(["nmcli","-g","common","dev","wifi"])
#res = res.decode('utf-8').split("\n")[1:-1]

"""for i in res:
    r = re.search(pattern, i)
    if r:
        print(r.groups()) """

res = res.decode('utf-8')
#print(pd.read_csv(res, sep='\t'))
#print(res)

from io import StringIO
import csv


f = StringIO(res)
#reader = csv.reader(f, delimiter=':')
#for row in reader:
 #   print(row)
prova = pd.read_csv(f, sep=':', header=None) #
prova.columns = ['CONNECTED','SSID','MODE','CHAN','RATE','SIGNAL','BARS','SECURITY']
#prova['CONNECTED'] = prova['CONNECTED'].map({'*':True})
#print(prova.columns)
prova.index = prova.index + 1
print(prova) 
