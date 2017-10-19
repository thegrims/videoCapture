import RPi.GPIO as gpio
import time

pins = [17,27]



def init():
    gpio.setmode(gpio.BCM)
    #for pin in pins:
        #(pin)
    #    gpio.setup(pin,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(27,gpio.OUT)

def forward(tf):
    init()
    for pin in pins:
       gpio.output(pin,True)
    #gpio.output(17,True)
    #gpio.output(27,True)
    stopAfter(tf)

def backward(tf):
    print("there's no going back Jim!")

def right(tf):
    init()
    gpio.output(17,True)
    gpio.output(27,False)
    stopAfter(tf)
    
def left(tf):
    init()
    gpio.output(17,False)
    gpio.output(27,True)
    stopAfter(tf)

def stopAfter(tf):
    time.sleep(tf)
    for pin in pins:
       gpio.output(pin,False)
    gpio.cleanup()
    
#forward(5)
#right(5)
#left(5)
