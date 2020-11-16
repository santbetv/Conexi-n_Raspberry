import requests
import json

API_ENDPOINT="https://apirestprof1cloaiza.herokuapp.com/"

urlautenticar="{0}{1}".format(API_ENDPOINT,"api/usuario/autenticar")
urlconsulta = "{0}{1}".format(API_ENDPOINT, "api/animal")



headers = {'Content-Type':'application/json'}

body = {'email':'carloaiza@umanizales.edu.co','password':'123456'}

respuesta= requests.post(urlautenticar, data=json.dumps(body), headers=headers)

#print(respuesta.status_code)
#print(json.loads(respuesta.content))

if respuesta.status_code >= 200 and respuesta.status_code <300:
    
    token = respuesta.json()['token']['access_token']
    #print(token)
    headers['Authorization']= "{0} {1}".format("Bearer", token)
    
    respconsulta = requests.get(urlconsulta, headers=headers)
    
    #print(json.loads(respconsulta.content))
    
    #pass
    #consumir el get animal
    if respuesta.status_code >= 200 and respuesta.status_code <300:
        print(json.loads(respconsulta.content))
    else:
        print("Error al consultar animales",respuesta.status_code,respuesta.content.decode('utf-8'))
    
else:
    print("Error token",respuesta.status_code,respuesta.content.decode('utf-8'))

