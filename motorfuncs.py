#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Assuming robot weight of 800g and 4 fresh AA batteries ###


### Distance travelled###

How far in seconds can it travel?

70cm every 2 seconds... 35cm per second. 
1m = 2.86 seconds

###turning circle###

How long for a 360 degree turn?

1.21 seconds!

180 degrees = 0.62

90 degrees = 0.31

"""
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM) # pin names (not physical numbers)
from time import sleep

in1_pin = 4
in2_pin = 17
in3_pin = 23
in4_pin = 24

GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
GPIO.setup(in3_pin, GPIO.OUT)
GPIO.setup(in4_pin, GPIO.OUT)
GPIO.setup(in4_pin, GPIO.OUT)
GPIO.setup(22, GPIO.OUT) 
GPIO.setup(25, GPIO.OUT) 

l_p = GPIO.PWM(25, 50) # Initialise PWM for the LEFT motor
r_p = GPIO.PWM(22, 50) # Initialise PWM for the RIGHT motor

# start it 'off' so the robot doesn't go off on its own.
l_p.start(0) 
r_p.start(0)

def map(x):
    """x is the number of degrees you with the robot to spin on the spot.
    0 == none - 360 == a full 360 degree spin"""
    ### Assuming robot weight of 800g and 4 fresh AA batteries ###
    return (x - 0) * (1.21 - 0) / (360 - 0) + 0

def speed(x):
    """set the speed of both motors together.
    0 == off - 100 == full"""
    l_p.ChangeDutyCycle(x)
    r_p.ChangeDutyCycle(x)
    
def stop():
    """Stops your robot should you need it to"""
    l_p.ChangeDutyCycle(0)
    r_p.ChangeDutyCycle(0)
    
def end():
    """Stops the robot and cleans up the GPIO pins - use to finish your program"""
    l_p.stop()
    r_p.stop()
    GPIO.cleanup()

def go_forward(x, y): 
    """Move the robot forward at x speed (0-100) for y seconds"""
    GPIO.output(in1_pin, True) 
    GPIO.output(in2_pin, False) 
    GPIO.output(in3_pin, True) 
    GPIO.output(in4_pin, False) 
    speed(x)
    sleep(y)

def go_back(x, y): 
    """Move the robot forward at x (0-100) speed for y seconds"""
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)
    GPIO.output(in3_pin, False)
    GPIO.output(in4_pin, True)
    speed(x)
    sleep(y)
    
def turn_right(x, y): 
    """Gradually turn your robot right, where x (0 == sharp turn to 100 == no turn) 
    relates to sharpness and y is the time the robot will continue to turn"""
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)
    GPIO.output(in3_pin, True) 
    GPIO.output(in4_pin, False) 
    l_p.ChangeDutyCycle(100)
    r_p.ChangeDutyCycle(x)
    sleep(y)
    
def turn_left(x, y):
    """Gradually turn your robot right, where x (0 == sharp turn to 100 == no turn) 
    relates to sharpness and y is the time the robot will continue to turn"""
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)
    GPIO.output(in3_pin, True) 
    GPIO.output(in4_pin, False) 
    l_p.ChangeDutyCycle(x)
    r_p.ChangeDutyCycle(100)
    sleep(y)

def spin_right(x):
    """Turns robot by number of degrees (from original facing direction)
    in a range between 0 and 360 degrees to the right"""
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)
    GPIO.output(in3_pin, True) # left motor forward
    GPIO.output(in4_pin, False) # left motor forward
    speed(100)
    sleep(map(x))

def spin_left(x):
    """Turns robot by number of degrees (from original facing direction)
    in a range between 0 and 360 degrees to the left"""
    GPIO.output(in1_pin, True) # right motor forward
    GPIO.output(in2_pin, False) # right motor forward
    GPIO.output(in3_pin, False)
    GPIO.output(in4_pin, True)
    speed(100)
    sleep(map(x))