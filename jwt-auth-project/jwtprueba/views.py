#from jwtprueba import app


#@app.route('/saludo')
#def saludo():
#    return 'Hola campeones'
import time
import json
import requests
from flask_jwt import jwt_required
from jwtprueba import app
from jwtprueba.EmulatorGUI import GPIO
from flask import request
from tkinter import *
from tkinter import messagebox



LEDS = {"green": 15, "red": 18}
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS["green"], GPIO.OUT)
GPIO.setup(LEDS["red"], GPIO.OUT)

@app.route('/')
def inicio():
    return 'Inicio de App REST'

@app.route('/saludo')
@jwt_required()
def saludo():
    return 'Hola campeones'

@app.route('/led/<color>/', methods=["GET", "POST"])
@jwt_required()
def api_leds_control(color):
    if request.method == "POST":
        if color in LEDS:
            #GPIO.output(18,True)
            GPIO.output(LEDS[color], int(request.data.get("state")))      
   
    return {color: GPIO.getStatePinOut(LEDS[color])}