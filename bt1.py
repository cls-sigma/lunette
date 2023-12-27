
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

redPin = 21
greenPin = 23
bluePin = 24


import time
import cv2
import threading
from talk import talk, audio
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






from vision import sentiment, analyse, localize_objects, ocr1, read, objects
import time                
            
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False



  
def vision1(param):

    vid = cv2.VideoCapture(0)

    t = " "
    c = 0
    while (True):

        ret, frame = vid.read()
        # cv2.imshow('frame', frame)
        if c == 1:
            
            audio("/home/pi/final_glass/camera.mp3")
            try:
              t += analyse(img=frame) + " \n"
              print(1)
            except:
                pass
            
            try:
               t += localize_objects(img=frame) + " \n"
               print(2)
            except:
                pass
            try:
                t += ocr1(content=frame) + " \n"
                print(3)
            except:
                pass
            try:
                t += sentiment(img=frame) + " \n"
                print(4)
            except:
                pass
            try:
                t += age_gender(content=frame) + " \n"
                print(4)
            except:
                pass
            break
        c += 1
        #time.sleep(1)

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    
    return t



import threading

def trea(fonction, param):
    a = threading.Thread(target=fonction, args=[param])
    a.start()
    
import time
from talk import talk
counter=0
b_etat1=0
while(True):
    
    etat1 = GPIO.input(bt1)
    etat2 = GPIO.input(bt2)
    print("b_etat1: ",b_etat1)
    if (etat2==0):
        time.sleep(2)
        if GPIO.input(bt2)==0:
            if b_etat1==1:
                talk('Mode navigation autonome activé')
                with open(path, "w") as f:
                    f.write('0')
                #trea(ranging, 1)
                b_etat1=0
            else:
                talk('Mode navigation autonome arrêté')
                with open(path, "w") as f:
                    f.write('1')
                b_etat1=1
            #trea(ranging, 0)
            print("Appui1 detecte")
        else:
            print("Appui2 detecte")
            audio("/home/pi/final_glass/audio.mp3")
            talk(vision1(1))
            
   

        # Temps de repos pour eviter la surchauffe du processeur
    time.sleep(0.5)
  
