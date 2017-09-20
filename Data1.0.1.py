import serial
import datetime
import time

ser = serial.Serial()
ser.baudrate = 230400
ser.port = '/dev/ttyUSB0'

ser.timeout = 8
ser.open()
a = 0
b = 0
c = -1
f = open("log.txt", "a+")

while 1:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%m-%d %H:%M:%S')
    data = ser.readline()
    a = data[3]
    if a != b:
        c = c + 1
    if a == "1":
        f.write(st + "C" + data)
    if a == "2":
        f.write(st + "D" + data)
    if a == "4":
        f.write(st + "W" + data)
    b = a
    print c
    f.flush()

f.close()
