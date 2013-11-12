pi-mation
=========
Stop motion animation app for RasPi and camera module (Python 2.7). 
This application was written by Russell Barnes for [Linux User & Developer magazine](http://www.linuxuser.co.uk) issue 134.

Dependencies
============
This application relies on [pygame](http://pygame.org) and [picamera](http://picamera.readthedocs.org).
You'll obviously need to be the proud owner of a Raspberry Pi camera module.

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

Usage
=====


    
