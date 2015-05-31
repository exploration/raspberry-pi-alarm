PiLarm
==========

Use a RaspberryPi as an all-in-one-box, motion-sensing alarm and notification system. Inspired by, and borrowing from, [this Make Article](http://makezine.com/projects/pilarm-portable-raspberry-pi-room-alarm/).

Uses code from:
- [Matrix Keypad](https://pypi.python.org/pypi/matrix_keypad) controller for the [Adafruit Matrix Keypad](https://www.adafruit.com/products/419)

To set up:

- Follow the wiring diagram in the `wiring_diagrams` folder to plug the physical devices together.
- Download the [latest version of Raspbian](https://www.raspberrypi.org/downloads/) (the Raspberry Pi operating system), and follow the [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md) on that page to copy it to an SD card. Make sure your SD card is at least 4GB.
- Use the [Adafruit Pi Finder Software](https://github.com/adafruit/Adafruit-Pi-Finder) to set up your Raspberry Pi.
- Once you have verified that the raspberry pi is accessible and booting up, you can move on:
- Then follow the instructions from [here](http://makezine.com/projects/pilarm-portable-raspberry-pi-room-alarm/), steps 2-5
  - Install GPIO (General Purpose Input/Output)
    - `sudo apt-get update`
    - `sudo apt-get install python-dev`
    - `sudo apt-get install python-rpi.gpio`
  - Install FSWebcam (to take photos)
    - `sudo apt-get install fswebcam`
  - Install MPG123 (to play MP3s)
    - `sudo apt-get install mpg123`
  - Install the actual PiLarm code:
    - `sudo apt-get install git-core`
    - `cd && git clone https://github.com/exploration/raspberry-pi-alarm`
    - Set the files to run on boot by adding the following two lines to `/etc/rc.local` just before the line that reads `exit 0`:
      - `sudo nano /etc/rc.local`, then...
      - `python /home/pi/raspberry-pi-alarm/keypadd.py &`
      - `python /home/pi/raspberry-pi-alarm/alarmd.py &`
  - Or you can do it all at once:
    - `sudo apt-get update && sudo apt-get install python-dev python-rpi.gpio fswebcam mpg123 git-core`
