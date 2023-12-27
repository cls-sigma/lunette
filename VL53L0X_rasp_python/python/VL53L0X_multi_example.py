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

from time import sleep
import time
import VL53L0X
import RPi.GPIO as GPIO


def ranging(param):
    # GPIO for Sensor 1 shutdown pin
    sensor1_shutdown = 20
    # GPIO for Sensor 2 shutdown pin
    sensor2_shutdown = 16

    vib1=12
    vib2=13
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    path="/home/pi/final_glass/config.txt"

    # Setup GPIO for shutdown pins on each VL53L0X

    GPIO.setup(sensor1_shutdown, GPIO.OUT)
    GPIO.setup(sensor2_shutdown, GPIO.OUT)

    GPIO.setup(vib1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(vib2, GPIO.OUT, initial=GPIO.LOW)

    pwmvib1 = GPIO.PWM(vib1, 100)
    pwmvib1.start(0)
    GPIO.output(vib1, GPIO.HIGH)

    pwmvib2 = GPIO.PWM(vib2, 100)
    pwmvib2.start(0)
    GPIO.output(vib2, GPIO.HIGH)

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
    time.sleep(0.80)
    tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

    # Set shutdown pin high for the second VL53L0X then 
    # call to start ranging 
    GPIO.output(sensor2_shutdown, GPIO.HIGH)
    time.sleep(0.80)
    tof1.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

    timing = tof.get_timing()
    if (timing < 20000):
        timing = 20000
    print ("Timing %d ms" % (timing/1000))
    count=1

    

    while(True):
        with open(path, "r") as f:
                print("read: ", f.read())
                if str(f.read())=='1':
                    break
        val1 = 0
        val2 = 0
        distance1 = tof.get_distance()
        if (distance1 > 0):
            print ("sensor %d - %d mm, %d cm, iteration %d" % (tof.my_object_number, distance1, (distance1/10), count))
            if 1<(distance1/10)< 100:
                    val1 = 100 - (distance1 / 10)
                    print("Val 1: " , val1 )
                    if val1 >0:
                        pwmvib1.ChangeDutyCycle(val1)
        else:
            print ("%d - Error" % tof.my_object_number)

        distance2 = tof1.get_distance()
        if (distance2 > 0):
            print ("sensor %d - %d mm, %d cm, iteration %d" % (tof1.my_object_number, distance2, (distance2/10), count))
            if 1<(distance2/10)< 100:
                    val2 = 100 - (distance2 / 10)
                    print("Val 2: " , val2 )
                    
                    if val2 >0:
                        pwmvib2.ChangeDutyCycle(val2)
        else:
            print ("%d - Error" % tof.my_object_number)

        #time.sleep(timing/1000000.00)
        time.sleep(1)
        pwmvib1.ChangeDutyCycle(0)
        pwmvib2.ChangeDutyCycle(0)

    tof1.stop_ranging()
    GPIO.output(sensor2_shutdown, GPIO.LOW)
    tof.stop_ranging()
    GPIO.output(sensor1_shutdown, GPIO.LOW)

ranging(2)