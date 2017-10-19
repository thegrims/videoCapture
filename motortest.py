import RPi.GPIO as gpio
import time
 
def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(27, gpio.OUT)
 
def forward(tf):
 init()
 gpio.output(17, True)
 gpio.output(27, True)
 time.sleep(tf)
 gpio.cleanup()
 
print("forward")
forward(5)

