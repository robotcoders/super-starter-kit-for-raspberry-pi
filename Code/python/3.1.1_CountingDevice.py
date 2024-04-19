#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

sensorPin = 26

SDI = 24
RCLK = 23
SRCLK = 18

placePin = (10, 22, 27, 17)
number = (0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f)

counter = 0

def clearDisplay():
    for i in range(8):
        GPIO.output(SDI, 0)
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)    

def hc595_shift(data): 
    for i in range(8):
        GPIO.output(SDI, 0x80 & (data << i))
        GPIO.output(SRCLK, GPIO.HIGH)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    GPIO.output(RCLK, GPIO.LOW)

def pickDigit(digit):
    for i in placePin:
        GPIO.output(i,GPIO.HIGH)
    GPIO.output(placePin[digit], GPIO.LOW)

def display():
    global counter                    
    clearDisplay() 
    pickDigit(0)  
    hc595_shift(number[counter % 10])

    clearDisplay()
    pickDigit(1)
    hc595_shift(number[counter % 100//10])

    clearDisplay()
    pickDigit(2)
    hc595_shift(number[counter % 1000//100])

    clearDisplay()
    pickDigit(3)
    hc595_shift(number[counter % 10000//1000])

def loop():
    global counter
    currentState = 0
    lastState = 0
    while True:
        display()
        currentState=GPIO.input(sensorPin)
        if (currentState == 0) and (lastState == 1):
            counter +=1
        lastState=currentState

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    for i in placePin:
        GPIO.setup(i, GPIO.OUT)
    GPIO.setup(sensorPin, GPIO.IN)

def destroy():   # When "Ctrl+C" is pressed, the function is executed.
    GPIO.cleanup()

if __name__ == '__main__':  # Program starting from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
