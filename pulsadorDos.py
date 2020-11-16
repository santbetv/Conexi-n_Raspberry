##import RPi.GPIO as GPIO
#importo libreria
from EmulatorGUI import GPIO
import requests
import time
import json

GPIO.setmode(GPIO.BCM)
#configuro pin 23 com entrada y activo
#esta activacion en la resistencia pin 23 con PUD_UP
#esto intrumpe tensión con voltaje 3.3v
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#  configuramos el pin 23 como salida para el led
GPIO.setup(24, GPIO.OUT)
# definimos dos variables para guardar el estado del led
# por defecto el estado del led es False (apagado)
switch_state=False
# por defecto el estado anterior es True (encendido)
old_input_state=True # activada
# bucle infinito que recoge el estado del pin18
# cada vez que presionamos el botón,el estado del switch
# alterna entre True/False
while True:
    # guardo en una variable el estado del pin
    new_input_state=GPIO.input(23)
    # si el estado es False (presionado),y el estado
    # anterior es True cambiamos el valor del switch
    if new_input_state == False and old_input_state == True:
        switch_state = not switch_state
        ##print('Boton presionado')
        ##print(switch_state)
        
        ########################PROCESO DE PETICION
        if switch_state==True:
            
            url = "https://gopidiego.site/api/auth/token"
            #url = "http://3.139.21.168:8069/api/auth/token"

            payload='login=rizzoli56@gmail.com&password=amorbb123&db=pruebas'
            headers = {
              'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            
            if response.status_code >= 200 and response.status_code <300:
                
                token= response.json()['access_token']
                
                
                
                url = "https://gopidiego.site/api/ganaderia.ganado/1"

                payload="{\n    \"accion_rasp\": \"aceptado\"\n}"
                headers = {
                'Content-Type': 'application/json'
                }
                
                headers['access_token'] = "{0}".format(token)
                respuestaPuesta = requests.request("PUT", url, headers=headers, data=payload)
                
                if respuestaPuesta.status_code >= 200 and respuestaPuesta.status_code <300:
                    
                    print("Activo la puerta")
                    
                    #GPIO.output(24, GPIO.HIGH)
                    GPIO.output(24, switch_state)
                    #print(token)
                else:
                    print("Fallo la solicitud al activar la puerta")
            else:
                print("Fallo la solicitud de token") 
        ########################FIN PROCESO DE PETICION

        
        # tiempo de demora para evitar rebote
        time.sleep(0.2)
    # guardamos el estado actual del GPIO24
    # old_input_state= new_input_state
    # modificamos el estado del led
    #GPIO.output(24, GPIO.LOW)
    GPIO.output( 24, switch_state)