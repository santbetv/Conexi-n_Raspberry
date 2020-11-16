#!/usr/bin/python
from flask import request
from flask_api import FlaskAPI
#import RPi.GPIO as GPIO
from EmulatorGUI import GPIO

LEDS = {"green": 15, "red": 18}

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS["green"], GPIO.OUT)
GPIO.setup(LEDS["red"], GPIO.OUT)

app = FlaskAPI(__name__)

@app.route('/', methods=["GET"])
def api_root():
 return { "led_url": request.url + "led/(green | red)/", "led_url_POST": {"state": "(0 | 1)"} }

@app.route('/led/<color>/', methods=["GET", "POST"])
def api_leds_control(color):
    if request.method == "POST":
        if color in LEDS:
            #GPIO.output(18,True)
            GPIO.output(LEDS[color], int(request.data.get("state")))      
   
    return {color: GPIO.getStatePinOut(LEDS[color])}
 
 #return { "led_url": request.url + "led/(green | red)/", "led_url_POST": {"state": "(0 | 1)"} }

if __name__ == "__main__":
 app.run()