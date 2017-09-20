#!/usr/bin/env python
import time
import serial


ser = serial.Serial(
port ='/dev/ttyUSB0',
baudrate = 230400,
)

f = open("file.txt", "w")

while True:
    data = serial.readline()
    f.write(data)
    f.flush()

f.close()
