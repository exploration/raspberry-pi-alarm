#!/usr/bin/python
#
# Modified by Donald Merand + Andy Smith for Explo
# http://www.explo.org
# http://github.com/exploration

import subprocess
import datetime
import time
import os 
import RPi.GPIO as io

io.setmode(io.BCM)

pir_pin = 18
flashingLight_pin = 7

io.setup(pir_pin, io.IN)
io.setup(flashingLight_pin, io.OUT)
io.output(flashingLight_pin, io.LOW)

# --------- Main Program ---------
previous_pir=0

while True:
	current_pir=io.input(pir_pin)	
	if previous_pir==0 and current_pir==1:
		with open("/home/pi/Alarm/armed.txt", "r") as fo:
      fo.seek(0, 0)
      status = fo.read(1)
      fo.closed
      print "Motion detected, armed status: " + str(status)
		if (status == "1"):
      subprocess.call("mpg123 /home/pi/Alarm/Audio/motiondetect.mp3", shell=True)
      time.sleep(10)
      with open("/home/pi/Alarm/armed.txt", "r") as fo:
        fo.seek(0, 0)
        status = fo.read(1)
        fo.closed 
		    if (status == "1"):
          print "Correct passcode not entered, emailing picture and sounding alarm."
          grab_cam = subprocess.Popen("sudo raspistill -w 640 -h 480 -o /home/pi/Alarm/Pictures/picture$RANDOM.jpg", shell=True)
          grab_cam.wait()

          io.output(flashingLight_pin, io.HIGH)
          subprocess.call("mpg123 /home/pi/Alarm/Audio/alarm.mp3", shell=True)
          subprocess.call("mpg123 /home/pi/Audio/Alarm/surrender.mp3", shell=True)
          subprocess.call("mpg123 /home/pi/Audio/Alarm/alarm.mp3", shell=True)                       
          io.output(flashingLight_pin, io.LOW)
          previous_pir=current_pir
          time.sleep(1)
