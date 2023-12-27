import cv2
import os
from talk import talk, audio
import threading
import re
import sys
import time
from time import sleep
import RPi.GPIO as GPIO
from time import sleep
#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
vib=13
redPin = 21
greenPin = 23
bluePin = 24
GPIO.setmode(GPIO.BCM)

GPIO.setup(vib, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)


pwmvibPin = GPIO.PWM(vib, 100)
pwmvibPin.start(0)
dutyCycle = 100
GPIO.output(vib, GPIO.HIGH)
GPIO.output(bluePin,GPIO.HIGH)

#talk("Initialisation du système.")
audio('/home/pi/final_glass/syste.wav')
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
        GPIO.output(bluePin,GPIO.LOW)
        #talk("Connection internete établie")
        audio('/home/pi/final_glass/connect.wav')
        break
    else:
        print("Not connected")
        GPIO.output(bluePin,GPIO.LOW)
        time.sleep(1)
        GPIO.output(bluePin,GPIO.HIGH)

import google
from googletrans import Translator
from google.cloud import vision
from google.cloud import speech
import smtplib
import ssl
from email.message import EmailMessage
from GoogleNews import GoogleNews
import wikipedia
import re
import twilio
import webbrowser
import pyaudio
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='/home/pi/final_glass/key.json'
'''
import pyautogui

#
'''
from six.moves import queue
global val
from face_client.face_client import FaceClient

api_key='ti9ubjrgmn3kpr8ldrc805ugd5'
api_secret="j1k96l3b4tv3cs009l1jdb1lkb"
client = FaceClient(api_key,api_secret)




def facial(content):
    att=""
    pat='/home/pi/final_glass/jkj.jpg'
    
    cv2.imwrite(pat, content)
    
    recog=client.faces_recognize('all', file=pat, namespace = 'visionplusadmin')


    #recog = client.faces_recognize('guido', file=path, namespace='visionplusadmin')
    #print(recog)
    response=recog['photos'][0]['tags']
    #print("response: ,", response)

    if len(response)>0:
        response=response[0]['uids']
        print("response: ,", response)
        try:
            response=response[0]['confidence']
            if int(response)>=30:
                att="admin"
            else:
                att="non"
        except:
            att="non"
    else:
        att="non"
    print("Réponse finale, ", att)
    return att

import mic
#talk("debut de la reconnaissance faciale")
"""audio('/home/pi/final_glass/face.wav')
pwmvibPin.ChangeDutyCycle(90)
sleep(2)
pwmvibPin.ChangeDutyCycle(0)
GPIO.output(vib, GPIO.LOW)

vid = cv2.VideoCapture(0)

text = ''                                                                                                                                                                                                                                                                                                                                                                                                               
compt=0
en=0
while (True):
    
    
    ret, frame = vid.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    '''if bre == 1:
        return 0'''
    result=""
    try:
        result=facial(content=frame)
    except Exception as e:
        print(e)
        
        
    if result=="admin":
        #talk("Bonjour administrateur")
        en=1
       
    #cv2.imshow('yur', frame)
    if en==1:
        print("Bonjour administrateur")
        
        GPIO.output(redPin,GPIO.LOW)
        GPIO.output(greenPin,GPIO.HIGH)
        GPIO.output(bluePin,GPIO.LOW)
        talk('Reconnaissance faciale reussie. Bonjour administrateur')
        audio("/home/pi/final_glass/admin.wav")
        vid.release()
        cv2.destroyAllWindows()
        break
import mic
        
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()"""
