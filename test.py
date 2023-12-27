
import time
#wh('93603836', 'Je vais pas pouvoir rentrer loo désolé loo')
b_etat1=0
b_etat2=0
bt1 = 29
bt2 = 31
# Iimport RPi.GPIO as GPIOnitialisation de la numerotation et des E/S
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(bt2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bt1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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