#!/usr/bin/python

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

from matrix_keypad import RPi_GPIO as MATRIX
import RPi.GPIO as GPIO
import pilarm
import subprocess
import time

# Set up the various lights
GPIO.setmode(GPIO.BCM)
GPIO.setup(pilarm.greenLED, GPIO.OUT)
GPIO.output(pilarm.greenLED, GPIO.HIGH) #turns the green LED on
GPIO.setup(pilarm.redLED, GPIO.OUT)
GPIO.output(pilarm.redLED, GPIO.LOW)    #turns the red LED off
GPIO.setup(pilarm.flashingLight, GPIO.OUT)
GPIO.output(pilarm.flashingLight, GPIO.LOW)  #turns the flashing light (powerswitch) off

  
# Initialize the keypad class
kp = MATRIX.keypad(columnCount = 3)

pilarm.setAlarmStatus(pilarm.alarmOff)
pilarm.playAudio("ready.mp3");

# Loop while waiting for a keypress
while True:
  digit = None
  while digit == None:
    digit = kp.getKey()

  # Print the result
  print digit
  pilarm.attempt = (pilarm.attempt[1:] + str(digit))  
  print pilarm.attempt

  if (pilarm.attempt == pilarm.passcode):
    #passcode match, check alarm status
    if (pilarm.getAlarmStatus() == pilarm.alarmOn):
      #system was armed, disarm it
      pilarm.setAlarmStatus(pilarm.alarmOff)
      GPIO.output(pilarm.greenLED, GPIO.HIGH)      #green LED on
      GPIO.output(pilarm.redLED, GPIO.LOW)         #red LED off
      GPIO.output(pilarm.flashingLight, GPIO.LOW)  #flashing light off (if applicable)
      pilarm.playAudio("disarmed.mp3")
    else:
      #system was disabled, and user intends to arm it
      GPIO.output(pilarm.greenLED, GPIO.LOW)       #green LED Off
      GPIO.output(pilarm.redLED, GPIO.HIGH)        #red LED on
      pilarm.playAudio("armed.mp3")
      time.sleep(10)
      pilarm.setAlarmStatus(pilarm.alarmOn)
  elif (pilarm.attempt == pilarm.haltcode):
    # halt code match, close down the entire keypad operation
    pilarm.playAudio("shutdown.mp3")
    subprocess.call("halt", shell=True)
    # also close down the alarm daemon
    subprocess.call("sudo killall alarmd.py", shell=True)
  
  # wait a half second, then try again
  time.sleep(0.5)
