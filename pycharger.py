#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
########################################################################
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
########################################################################

import os, sys
import time
import serial

# discharge end voltage (empty)

dchg_end = 3.2


# iCharger modes of operation
mop=[None]*13

mop[1]  = "Charging"
mop[2]  = "Discharging"
mop[3]  = "Monitor"
mop[4]  = "Waiting"
mop[5]  = "Motor burn-in"
mop[6]  = "Finished"
mop[7]  = "Error"
mop[8]  = "LIxx trickle"
mop[9]  = "NIxx trickle"
mop[10] = "Foam cut"
mop[11] = "Info"
mop[12] = "External-discharging"

# configure the serial connections
# change according to the ttyUSB assigned to the iCharger (dmesg)

ser = serial.Serial(
    port='/dev/ttyUSB0',
)

ser.open()
ser.isOpen()

### MAIN #############################################################

while 1 :

    line    = ser.readline  ()
    raw     = line.split    (';')

    v_bat   = float         (raw[4])/1000
    v_c1    = float         (raw[6])/1000
    v_c2    = float         (raw[7])/1000
    v_c3    = float         (raw[8])/1000
    v_in    = float         (raw[3])/1000
    i_chg   = int           (raw[5])*10
    i_sum   = float         (raw[18])/1000
    t_int   = float         (raw[16])/10
    t_ext   = float         (raw[17])/10

    s_vc1   = ((float       (raw[6])/1000)-dchg_end)*100
    s_vc2   = ((float       (raw[7])/1000)-dchg_end)*100
    s_vc3   = ((float       (raw[8])/1000)-dchg_end)*100
    s_bat   = round         ((((float(raw[4])/1000)
            -               (dchg_end*3))*100/3), 1)

    print "Mode:           " + mop[int(raw[1])]
    print "Batt:           " + str(v_bat) + " V (" + str(s_bat) + "%)"
    print "Cell 1:         " + str(v_c1) + " V (" + str(s_vc1) + "%)"
    print "Cell 2:         " + str(v_c2) + " V (" + str(s_vc2) + "%)"
    print "Cell 3:         " + str(v_c3) + " V (" + str(s_vc3) + "%)"
    print "Supply:         " + str(v_in) + " V"
    print "Charge Current: " + str(i_chg) + " mA"
    print "Charge Amount:  " + str(i_sum) + " A"
    print "Temp INT:       " + str(t_int) + " °C"
    print "Temp EXT:       " + str(t_ext) + " °C"
    print ">>" + line
