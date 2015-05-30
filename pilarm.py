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
greenLED      = 16
redLED        = 21
flashingLight = 6
pirSensor     = 22

# Set some keypad + alarm values
alarmOff = "0"
alarmOn  = "1"
attempt  = "0000"
passcode = "4444"    
haltcode = "5555"


# handy function which we will use to play audio all over the place
def playAudio(filename):
  subprocess.call("mpg123 /home/pi/raspberry-pi-alarm/audio/" + filename, shell=True)

# function to get the status of the alarm
def getAlarmStatus():
  with open("/home/pi/Alarm/armed.txt", "r+") as fo:
    fo.seek(0, 0)
    status = fo.read(1)
  fo.closed
  return str(status)

# function to set the status of the alarm
def setAlarmStatus(status):
  with open("/home/pi/Alarm/armed.txt", "r+") as fo:
    fo.seek(0, 0)
    fo.write(status)
  fo.closed
