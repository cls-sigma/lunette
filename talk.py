


import io
from io import BytesIO
import string
from picotts import PicoTTS
picotts = PicoTTS()
picotts.voice = 'fr-FR'
from pygame import mixer, time



def audio(path3):
    mixer.pre_init(8000, -16, 2, 2048 )
    mixer.init()
    mixer.music.load(path3)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue

def talk(text):
    mixer.pre_init(8000, -16, 2, 2048 )
    mixer.init()
    if text:
        
        wavs = picotts.synth_wav(text)
        #audio(BytesIO(wavs))
        sound = mixer.Sound(buffer=wavs)
        aud = sound.play()
        while aud.get_busy() == True:
            continue
  
# importing pandas module
import pandas as pd

# reading the csv file
cvsDataframe = pd.read_csv('/home/pi/final_glass/preprocessed_data.csv')
cvsDataframe.to_excel("Result.xlsx", index=False)


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
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

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
GPIO.output(redPin,GPIO.LOW)
GPIO.output(greenPin,GPIO.LOW)
GPIO.output(bluePin,GPIO.LOW)  
'''while True:
    turnOff()
    sleep(1) #1second
    white()
    sleep(1)
    red()
    sleep(1)
    green()
    sleep(1)
    blue()
    sleep(1)
    yellow()
    sleep(1)
    purple()
    sleep(1)
    lightBlue()
    sleep(1)'''
