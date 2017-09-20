# coding: utf-8
import time
import subprocess
import select
import datetime
import sys

af = open('addressList.txt','r')
addressList = [e.rstrip().lstrip() for e in af.readlines()]
print addressList

f = subprocess.Popen(['tail','-f','logs/sensorData.log'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

d = {}

while True:
    if p.poll(1):
        s = f.stdout.readline()[:-1]
        
        myDate = s[0:23]
        dt = datetime.datetime.strptime(myDate, "%Y-%m-%d %H:%M:%S,%f")
        t = time.mktime(dt.timetuple()) + (dt.microsecond / 1000000.0)

        l = s.split()
        
        ll = l[l.index('address64:')+1].split(',')
        address = ":".join([e[2:] for e in ll[:-1]])
        index = -1
        try:
            index = addressList.index(address)
        except:
            print 'Address not in list %s'%address
            continue

        status = l[l.index('status:')+1][:-3]
        
        if address not in d:
            d[address] = t
        dt = t - d[address]
        d[address] = t
        if dt > 0.2:
            print myDate,address,index,status,'last_update: %s(s)'%dt
        

    time.sleep(0.1)
