# coding: utf-8
import serial
from xbee import ZigBee
import binascii
import time

ser = serial.Serial('/dev/tty.usbserial-A6XXHBGT', 9600)
zb = ZigBee(ser)

f = open("addressList.txt",'r')
addressList = [bytearray.fromhex(e.rstrip().lstrip().replace(':',' ')) for e in f.readlines()]

for i in range(len(addressList)):
    print binascii.hexlify(addressList[i])
    '''
    zb.remote_at(dest_addr_long=addressList[i],command='RE')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='ID',parameter='\xFF\xFE')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='SM',parameter='\x04')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='SP',parameter='\x01\xF4')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='ST',parameter='\x03\xE8')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='PO',parameter='\x0A')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='D0',parameter='\x03')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='IR',parameter='\x01\xF4')
    time.sleep(0.1)
    zb.remote_at(dest_addr_long=addressList[i],command='NI',parameter='E%s'%(i+1))
    '''
    zb.remote_at(dest_addr_long=addressList[i],command='DH',parameter='\x00')
    time.sleep(0.5)
    zb.remote_at(dest_addr_long=addressList[i],command='DL',parameter='\x00')
    time.sleep(0.5)
    zb.remote_at(dest_addr_long=addressList[i],command='WR')
    time.sleep(0.5)

print "Finish Resetting! Close serial"
ser.close()

