#!/usr/bin/python

# MIT License
#
# Copyright (c) 2017 John Bryan Moore
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X
import RPi.GPIO as GPIO

# GPIO for Sensor 1 shutdown pin
sensor1_shutdown = 20
# GPIO for Sensor 2 shutdown pin
sensor2_shutdown = 16
import RPi.GPIO as GPIO
from time import sleep
path="/home/pi/final_glass/config.txt"
# Vibrate PWM pins: GPIO 12(32), GPIO 13(33), GPIO 18(12), GPIO 19(35).

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
vib1 = 12
vib2 = 13


GPIO.setwarnings(False)
# Setup GPIO for shutdown pins on each VL53L0X
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1_shutdown, GPIO.OUT)
GPIO.setup(sensor2_shutdown, GPIO.OUT)
# Vib pins:
GPIO.setup(vib1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(vib2, GPIO.OUT, initial=GPIO.LOW)

pwmvib1 = GPIO.PWM(vib1, 100)
pwmvib2 = GPIO.PWM(vib2, 100)
pwmvib1.start(0)
pwmvib2.start(0)
GPIO.output(vib1, GPIO.HIGH)
GPIO.output(vib2, GPIO.HIGH)

# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(sensor1_shutdown, GPIO.LOW)
GPIO.output(sensor2_shutdown, GPIO.LOW)

# Keep all low for 500 ms or so to make sure they reset
time.sleep(0.50)

# Create one object per VL53L0X passing the address to give to
# each.
tof = VL53L0X.VL53L0X(i2c_address=0x2B)
tof1 = VL53L0X.VL53L0X(i2c_address=0x2D)
tof.open()
tof1.open()

# Set shutdown pin high for the first VL53L0X then
# call to start ranging
GPIO.output(sensor1_shutdown, GPIO.HIGH)
time.sleep(0.50)
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

# Set shutdown pin high for the second VL53L0X then
# call to start ranging
GPIO.output(sensor2_shutdown, GPIO.HIGH)
time.sleep(0.50)
tof1.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing / 1000))

count = 0
def ranging(param):
    while (True):
        val1 = 0
        val2 = 0
        distance1 = tof.get_distance()
        print(distance1)
        if distance1 > 0:
            print("sensor %d - %d mm, %d cm, iteration %d" % (1, distance1, (distance1 / 10), count))
            if 1000 > distance1:
                val1 = 819 - (distance1 / 10)
                pwmvib1.ChangeDutyCycle(val1)
    
        else:
            print("%d - Error" % 1)
    
        distance2 = tof1.get_distance()
        print(distance2)
        if distance2 > 0:
            print("sensor %d - %d mm, %d cm, iteration %d" % (2, distance2, (distance2 / 10), count))
            if 1000 > distance2:
                val2 = 819 - (distance2 / 10)
                pwmvib2.ChangeDutyCycle(val2)
        else:
            print("%d - Error" % 2)
    
        # time.sleep(timing/1000000.00)
        time.sleep(0.5)
        pwmvib1.ChangeDutyCycle(val1)
        pwmvib2.ChangeDutyCycle(val2)
        with open(path, "r") as f:
            if str(f.read())=="1":
                break
    with open(path, "w") as f:
        f.write('0')
    tof1.stop_ranging()
    GPIO.output(sensor2_shutdown, GPIO.LOW)
    tof.stop_ranging()
    GPIO.output(sensor1_shutdown, GPIO.LOW)
    tof.close()
    tof1.close()


ranging(2)
'''
import time
import VL53L0X
import RPi.GPIO as GPIO

# GPIO for Sensor 1 shutdown pin
sensor1_shutdown = 20
# GPIO for Sensor 2 shutdown pin
sensor2_shutdown = 16

GPIO.setwarnings(False)

# Setup GPIO for shutdown pins on each VL53L0X
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1_shutdown, GPIO.OUT)
GPIO.setup(sensor2_shutdown, GPIO.OUT)

# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(sensor1_shutdown, GPIO.LOW)
GPIO.output(sensor2_shutdown, GPIO.LOW)

# Keep all low for 500 ms or so to make sure they reset
time.sleep(0.50)

# Create one object per VL53L0X passing the address to give to
# each.
tof = VL53L0X.VL53L0X(address=0x2B)
tof1 = VL53L0X.VL53L0X(address=0x2D)

# Set shutdown pin high for the first VL53L0X then 
# call to start ranging 
GPIO.output(sensor1_shutdown, GPIO.HIGH)
time.sleep(0.50)
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

# Set shutdown pin high for the second VL53L0X then 
# call to start ranging 
GPIO.output(sensor2_shutdown, GPIO.HIGH)
time.sleep(0.50)
tof1.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

for count in range(1,101):
    distance = tof.get_distance()
    if (distance > 0):
        print ("sensor %d - %d mm, %d cm, iteration %d" % (tof.my_object_number, distance, (distance/10), count))
    else:
        print ("%d - Error" % tof.my_object_number)

    distance = tof1.get_distance()
    if (distance > 0):
        print ("sensor %d - %d mm, %d cm, iteration %d" % (tof1.my_object_number, distance, (distance/10), count))
    else:
        print ("%d - Error" % tof.my_object_number)

    time.sleep(timing/1000000.00)

tof1.stop_ranging()
GPIO.output(sensor2_shutdown, GPIO.LOW)
tof.stop_ranging()
GPIO.output(sensor1_shutdown, GPIO.LOW)'''