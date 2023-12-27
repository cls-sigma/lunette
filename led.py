#https://www.codespeedy.com/how-to-check-the-internet-connection-in-python/
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

#from vision import sentiment, analyse, localize_objects, ocr1, read, objects
#from VL53L0X_multi_example import ranging
from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
import time
import cv2
import threading
from talk import talk
path=u"/home/pi/final_glass/config.txt"
path2=u'/home/pi/final_glass/vision.txt'
with open(path, "w") as f:
    f.write('0')
with open(path2, "w") as f:
    f.write('0')

global b_etat1
global b_etat2
b_etat1=0
b_etat2=0
bt1 = 5
bt2 = 6
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

GPIO.setup(bt2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bt1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def audio(path3):
    play(AudioSegment.from_file(path3))
    


def turnOff():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)
    
def white():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
def red():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def green():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def blue():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def yellow():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def purple():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def lightBlue():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    

import time                
            
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

GPIO.output(redPin,GPIO.LOW)
GPIO.output(greenPin,GPIO.LOW)
GPIO.output(bluePin,GPIO.LOW)
#from VL53L0X_multi_example import ranging
from talk import talk
var=10
while(True):
    if connect():
        #var=0
        print("Yes")
        if var==0:
            pass
        else:
            print("yes")
            GPIO.output(redPin,GPIO.LOW)
            GPIO.output(greenPin,GPIO.HIGH)
            GPIO.output(bluePin,GPIO.LOW)
            talk('Connection internet établie')
        var=0
    else:
        
        if var==1:
            pass
        else:
            print("Fasle")
            GPIO.output(redPin,GPIO.LOW)
            GPIO.output(greenPin,GPIO.LOW)
            GPIO.output(bluePin,GPIO.HIGH)
            time.sleep(4)
            talk('Déconnecté')
        var=1

