
#https://stackoverflow.com/questions/67241180/installing-pico-tts-german-language-on-raspberry-pi
#pip install py-picotts ttspico
#Pygame Play sound: https://projects.raspberrypi.org/en/projects/generic-python-playing-sound-files

# Automatic programm init: @reboot sleep 60 && sudo python /home/pi/
import wave
import io
from io import BytesIO
import string
from picotts import PicoTTS
#import pygame
#pygame.init()
from pydub import AudioSegment
from pydub.playback import play
picotts = PicoTTS()
picotts.voice = 'fr-FR'

def audio(path3):
    play(AudioSegment.from_file(path3))


def talk(text):
    if text:
        wavs = picotts.synth_wav(text)
        audio(BytesIO(wavs))
    else:
        pass
    #wav = wave.open(BytesIO(wavs))
    
    #print(wav.getnchannels(), wav.getframerate(), wav.getnframes())
    #with open("hi.wav", "wb") as f:
    #f.write(wavs)
    #my_sound = pygame.mixer.Sound('hi.wav')
    #my_sound.play()
#libraries
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