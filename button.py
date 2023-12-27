# Import des modules
# Il faut connecter les broches des buttons au
# 3.3v via une resistance de 10k: http://electroniqueamateur.blogspot.com/2015/10/scratch-sur-raspberry-pi-2-bouton.html
# Numéro des GPIO en mode board: https://fr.pinout.xyz/
# https://www.raspberryme.com/gpio-et-python-4-9-bouton-poussoir/
from vision import sentiment, analyse, localize_objects, ocr1, read, objects
#from VL53L0X_multi_example import ranging
from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
import time
import cv2
import threading
from talk import talk
path="/home/pi/final_glass/config.txt"
path2='/home/pi/final_glass/vision.txt'
with open(path, "w") as f:
    f.write('0')
with open(path2, "w") as f:
    f.write('0')

b_etat1=0
b_etat2=0
bt1 = 5
bt2 = 6
# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BCM)
GPIO.setup(bt2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bt1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def trea(fonction, param):
    a = threading.Thread(target=fonction, args=[param])
    a.start()

def audio(path3):
    play(AudioSegment.from_file(path3))
def ranging():
    pass

def vision():
    # define a video capture object
    vid = cv2.VideoCapture(0)
    talk("capture dans quelques secondes")
    t = " "
    c = 0
    while (True):

        ret, frame = vid.read()
        # cv2.imshow('frame', frame)
        if c == 3:
            audio("/home/pi/final_glass/camera.mp3")
            t += analyse(content=frame) + " \n"
            t += localize_objects(content=frame) + " \n"
            try:
                t += ocr(content=frame) + " \n"
            except:
                pass
            try:
                t += sentiment(content=frame) + " \n"
            except:
                pass
            break
        c += 1
        time.sleep(1)

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return t

# Si on detecte un appui sur le bouton, on allume la LED
# et on attend que le bouton soit relache

while True:

    etat1 = GPIO.input(bt1)
    etat2 = GPIO.input(bt2)
    
    if (etat1 == 0):
        '''if b_etat1==1:
            talk('Mode navigation autonome activé')
            with open(path, "w") as f:
                f.write('0')
            trea(ranging, 1)
            b_etat1=0
        else:
            talk('Navigation autonome arreté')
            with open(path, "w") as f:
                f.write('1')
            b_etat1=1'''
        print("Appui1 detecte")
        # GPIO.output(16,True)
    else:
        # GPIO.output(16, False)
        print("relaché1")
    if (etat2 == 0):
        print("Appui2 detecte")
        # GPIO.output(16,True)
    else:
        # GPIO.output(16, False)
        print("relaché2")

        # Temps de repos pour eviter la surchauffe du processeur
    time.sleep(1)

