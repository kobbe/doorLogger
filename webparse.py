#!/usr/bin/env python3.2  

#stats for moebius.nu/state.php once a minute

from urllib.request import urlopen
import time
import datetime



x = 'e'
try:
    for line in urlopen('http://mooebius.mooo.com/state.php',timeout = 40):
        line = line.decode('utf-8')
        if 'closed' in line:
            x = 'c'
        elif 'open' in line:
            x = 'o'
    now = datetime.datetime.now()
    with open('/home/pi/Desktop/Python/values.txt', 'a') as f:
        f.write(now.strftime("%Y%m%d%H%M%S")+x+"\n")
except BaseException:
    x = 'e'
    now = datetime.datetime.now()
    with open('/home/pi/Desktop/Python/errorlog.txt', 'a') as f:
        f.write(now.strftime("%Y%m%d%H%M%S")+x+"\n")
    with open('/home/pi/Desktop/Python/values.txt', 'a') as f:
        f.write(now.strftime("%Y%m%d%H%M%S")+x+"\n")

