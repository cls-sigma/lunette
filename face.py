
import cv2
import os

from talk import talk
import threading
import re
import sys
import time
import RPi.GPIO as GPIO
from time import sleep
#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BCM)
#set red,green and blue pins
redPin = 21
greenPin = 23
bluePin = 24
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

 
GPIO.output(redPin,GPIO.LOW)
GPIO.output(greenPin,GPIO.LOW)
GPIO.output(bluePin,GPIO.HIGH)
 
talk("Initialisation du système.")
import time                
            
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
while True:
    if connect():
        GPIO.output(redPin,GPIO.HIGH)
        GPIO.output(greenPin,GPIO.LOW)
        GPIO.output(bluePin,GPIO.LOW)
        talk("Connection internete établie")
        break
    else:
        print("Not connected")
        GPIO.output(bluePin,GPIO.LOW)
        time.sleep(1)
        GPIO.output(bluePin,GPIO.HIGH)
from  datetime import datetime
print(datetime.now())


import google
from googletrans import Translator
from google.cloud import vision
from google.cloud import speech
#import numpy as np
#import pandas as pd

from GoogleNews import GoogleNews
import wikipedia


import pyaudio
from six.moves import queue
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='/home/pi/final_glass/key.json'
global val
# talk("Initialisation")

from email.message import EmailMessage
import smtplib
import ssl

import webbrowser
import pyautogui
import re

from twilio.rest import Client


print("Import sucessfull")


import mic
