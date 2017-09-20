# coding: utf-8
import serial
from xbee import ZigBee
import binascii
import time

dev = '/dev/tty.usbserial-DA01MHJT'
ser = serial.Serial(dev, 9600)
zb = ZigBee(ser)

f = open("addressList.txt",'r')
addressList = [bytearray.fromhex(e.rstrip().lstrip().replace(':',' ')) for e in f.readlines()]

for i in range(len(addressList)):
    print binascii.hexlify(addressList[i])
    print "OFF",i
    zb.remote_at(dest_addr_long=addressList[i],command='D4',parameter='\x04')
    time.sleep(0.5)
    #print "ON",i
    #zb.remote_at(dest_addr_long=addressList[i],command='D4',parameter='\x05')

print "Finish Resetting! Close serial"
ser.close()

