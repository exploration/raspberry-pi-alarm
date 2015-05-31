#######################################################################
# PiLarm
#
# Original concept by Jeff Highsmith
# http://makezine.com/projects/pilarm-portable-raspberry-pi-room-alarm/
# 
# Written by Donald Merand + Andy Smith for Explo
# http://www.explo.org
# http://github.com/exploration
#######################################################################


#######################################################################
# This file contains the setup variables + configuration for the PiLarm
#######################################################################

import os
import subprocess

# Set the GPIO pins for our lights + sensors
greenLED         = 15 #RXD
redLED           = 14 #TXD
flashingLight    = 10 #MOSI
pirSensor        = 22

# Set some keypad + alarm values
alarmOff         = "0"
alarmOn          = "1"
attempt          = "0000"
passcode         = "4444"    
haltcode         = "5555"
countdownSeconds = 10


# handy function which we will use to play audio all over the place
def playAudio(filename):
  subprocess.call("mpg123 /home/pi/raspberry-pi-alarm/audio/" + filename, shell=True)

# function to get the status of the alarm
def getAlarmStatus():
  with open("/home/pi/raspberry-pi-alarm/armed.txt", "r+") as fo:
    fo.seek(0, 0)
    status = fo.read(1)
  fo.closed
  return str(status)

# function to set the status of the alarm
def setAlarmStatus(status):
  with open("/home/pi/raspberry-pi-alarm/armed.txt", "r+") as fo:
    fo.seek(0, 0)
    fo.write(status)
  fo.closed
