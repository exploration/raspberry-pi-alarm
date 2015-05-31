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
import datetime
import pilarm
import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(pilarm.pirSensor, GPIO.IN)
# though this file can activate the flashing light, the alarmd.py file takes
# care of the initialization of that light, so we skip it here


# --------- Main Program ---------
previousPir = 0

# loop FOREVER
while True:
  # check value of PIR sensor
  currentPir = GPIO.input(pilarm.pirSensor)	
  if previousPir == 0 and currentPir == 1:
    # movement happened since last check, see if the alarm is set
    status = pilarm.getAlarmStatus()
    print "Motion detected, armed status: " + status 
    if (status == "1"):
      # alarm is set, warn the house
      pilarm.playAudio("motiondetect.mp3")
      # wait for 10 seconds while keypadd.py determines whether user is
      # correctly entering the password
      time.sleep(10)
      # check to see if disarm was successful
      status = piLarm.getAlarmStatus()
      if (status == "1"):
        # still armed, password was not correctly entered
        print "Correct passcode not entered, sounding alarm"
        grab_cam = subprocess.Popen("sudo raspistill -w 640 -h 480 -o /home/pi/raspberry-pi-alarm/pictures/picture$RANDOM.jpg", shell=True)
        grab_cam.wait()

        GPIO.output(pilarm.flashingLight, GPIO.HIGH)
        pilarm.playAudio("alarm.mp3")
        pilarm.playAudio("surrender.mp3")
        pilarm.playAudio("alarm.mp3")
        GPIO.output(pilarm.flashingLight, GPIO.LOW)

  # now just continue on our merry way
  previousPir = currentPir
  # wait a little bit, then try again
  time.sleep(0.5)
