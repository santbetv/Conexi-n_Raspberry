##import RPi.GPIO as GPIO
from EmulatorGUI import GPIO
import time
##Coloco mis pin de salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#genero el ciclo para el semaforo 14 15 18
while True:
   GPIO.output(14, GPIO.HIGH)
   GPIO.output(15, GPIO.LOW)
   GPIO.output(18, GPIO.LOW)
   time.sleep(5)
   GPIO.output(14, GPIO.LOW)
   GPIO.output(15, GPIO.HIGH)
   GPIO.output(18, GPIO.LOW)
   time.sleep(1)
   GPIO.output(14, GPIO.LOW)
   GPIO.output(15, GPIO.LOW)
   GPIO.output(18, GPIO.HIGH)
   time.sleep(5)
    
    