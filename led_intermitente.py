##import RPi.GPIO as GPIO
from EmulatorGUI import GPIO
import time

#asigno el nodo al puerto GPIO
GPIO.setmode(GPIO.BCM)
# Configuro si el pin es entrada o salida
GPIO.setup(7, GPIO.OUT)

while True:
    # envio la señal por ese puerto
   GPIO.output(7, True)
   time.sleep(1)
   GPIO.output(7, False)
   time.sleep(1)