#from flask import Flask

#app = Flask(__name__)

#import jwtprueba.views
from flask_api import FlaskAPI
#from flask import Flask
from jwtprueba.database import init_db, shutdown_db_session

app = FlaskAPI(__name__)

import jwtprueba.views
import jwtprueba.jwt
#import jwtprueba.EmulatorGUI


init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    shutdown_db_session()





