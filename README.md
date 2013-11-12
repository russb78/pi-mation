pi-mation
=========
Stop motion animation app for RasPi and camera module (Python 2.7). 

This application was written by Russell Barnes for [Linux User & Developer magazine](http://www.linuxuser.co.uk) issue 134.

Dependencies & installation
===========================
This application relies on [pygame](http://pygame.org) and [picamera](http://picamera.readthedocs.org).
You'll obviously need to be the proud owner of a Raspberry Pi camera module too.

If you haven't used your camera module yet you'll need to make sure your Pi is up to date
and the camera module is initialised:

    sudo apt-get update && sudo apt-get upgrade
    sudo raspi-config
    
In the Raspberry Pi config screen you'll need to select option 5 to enable the camera.


You can install the Python library to control the Pi camera at the command line with:

    sudo apt-get install python-setuptools
    easy_install picamera

Pygame can be installed with the following command:

    sudo apt-get install python-pygame

For making and watching videos the application uses libav-tools and omxplayer respectively. 
Ensure they're installed with:

    sudo apt-get install libav-tools && sudo apt-get install omxplayer

From the terminal type:

    sudo apt-get install git

Once installed you can clone this repository with the clone command:

    cd~
    git clone https://github.com/russb78/pi-mation.git

Now you can enter the pi-mation sub-directory and run pi-mation.py with the following commands:

    cd pi-mation/pi-mation
    python pi-mation.py

Usage
=====
Could you be the next [Nick Park](http://en.wikipedia.org/wiki/Nick_Park)? 
Try your hand at stop motion animation with this simple, but effective RasPi application.

![Test](pi-mation/data/start_screen.jpg)

    
