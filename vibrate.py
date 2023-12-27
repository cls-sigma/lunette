import RPi.GPIO as GPIO
from time import sleep
#PWM pins: GPIO 12(32), GPIO 13(33), GPIO 18(12), GPIO 19(35).
ledPin = 32
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
pwmLEDPin = GPIO.PWM(ledPin, 100)
pwmLEDPin.start(0)
dutyCycle = 100
GPIO.output(ledPin, GPIO.HIGH)
c=5
pwmLEDPin.ChangeDutyCycle(0)
while True:
        pwmLEDPin.ChangeDutyCycle(dutyCycle)
        
        if dutyCycle == 100:
            c=-5
        elif dutyCycle ==5:
            c=5
                 
        dutyCycle += c
        sleep(0.25)
        print(dutyCycle)
        