
# coding: utf-8

# In[93]:

get_ipython().magic(u'pylab inline')
import numpy as np


# In[94]:

import datetime


# #Coordinator log

# In[95]:

f = open("battery_testing/coordinator1.txt","r")
data1 = f.readlines()


# In[96]:

t = []
for d in data1[70:-10]:
    time = datetime.datetime.strptime(d[0:23], "%Y-%m-%d %H:%M:%S,%f")
    t.append(time)


# In[97]:

dt = [x.total_seconds() for x in np.diff(t)]

plt.figure(figsize=(14,8))
plt.plot(t[:-1],dt)

plt.title("Time Difference between 2 data received\nFrom 7.30pm 27/12 to 12.30pm on 29/12/2015")
plt.grid()


# In[134]:

print (t[-1]-t[0])/60/60


# In[98]:

plt.figure(figsize=(16,8))
plt.plot(t,np.zeros(len(t)),'x')
plt.grid()


# #Sensor Log

# In[124]:

f.close()
f1 = open("battery_testing/sensor1.txt","r")
START_TIME = 10000


# In[125]:

data = f1.readlines()


# In[126]:

t = []
on_duration = []
for s in data:
    if s.find("[OFF] ON_DURATION")!=-1:
        l = s.split(" ")
        time = float(l[0][1:])
        if time>START_TIME:
            t.append(float(l[0][1:]))
            on_duration.append(int(l[-1]))
        


# In[130]:

plt.figure(figsize=(16,8))
plt.plot(t,on_duration,'b.')
plt.grid()
plt.title("XBEE ON_DURATION")
plt.xlabel("time (s)")
plt.ylabel("ON_DURATION (ms)")


# In[138]:

t = []
retry = []
deliver = []
for s in data:
    if s.find("[TX]")!=-1:
        l = s.split(" ")
        time = float(l[0][1:])
        if time>START_TIME:
            t.append(time)
            try: 
                retryCount = int(l[4].split("=")[1][:-1],16)
                deliveryStatus = int(l[3].split("=")[1][:-1],16)
            except:
                print l
            retry.append(retryCount)
            deliver.append(deliveryStatus)
            
            


# In[140]:

plt.figure(figsize=(14,6))
plt.grid()
plt.title("retryCount")
plt.plot(t,retry,'b.')
plt.xlabel("time (s)")
plt.ylabel("retry")
plt.ylim(-1,5)


# In[141]:

plt.figure(figsize=(14,6))
plt.grid()
plt.title("deliveryStatus")
plt.xlabel("time (s)")
plt.ylabel("statusCode")
# plt.ylim(-1,5)
plt.plot(t,deliver,'b.')


# #Coulomb Counter

# In[156]:

f.close()
f2 = open("battery_testing/battery1.txt","r")
START_TIME = 10000


# In[157]:

data2 = f2.readlines()


# In[161]:

t = []
mA = []
for s in data2[7:]:
    l = s.split(" ")
    time = float(l[0][1:])
    if time>START_TIME:
        t.append(time)
        mA.append(float(l[-1]))


# In[172]:

plt.figure(figsize=(14,6))
plt.grid()
plt.title("Average Current using Coulomb Counter")
plt.plot(t,mA)
plt.xlabel("time (s)")
plt.ylabel("Average Current (mA)")
# plt.ylim(0.4,0.8)


# In[ ]:



