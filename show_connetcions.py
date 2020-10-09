#!/usr/bin/env python3

import subprocess 

result = subprocess.check_output(["nmcli","-f","SSID","dev","wifi"])
result = result.decode('utf-8')

result = result.split('\n')

for x in result[1:]:
    print(x)