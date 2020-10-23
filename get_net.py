#!/usr/bin/env python3

import subprocess 
import json 
from pprint import pprint

res = subprocess.check_output(["ip","-j","a"])
dec = json.loads(res.decode("utf-8"))

for d in dec:
    #pprint(d)
    #if d["addr_info"]['family'] == 'inet':
    #    pprint(d["addr_info"]) 
    for a in d['addr_info']:
        if a['family'] == 'inet':
            print(a['label'], end=':')
            print(a['local'])