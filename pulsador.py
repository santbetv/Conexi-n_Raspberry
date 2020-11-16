##import RPi.GPIO as GPIO
from EmulatorGUI import GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

while True:
   if GPIO.input(14):
      GPIO.output(15, False)
   else:
      GPIO.output(15, True)