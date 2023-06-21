from flask import Flask
from flask_restful import Api
from config import conexion
from flask_migrate import Migrate
from models.usuario_model import UsuarioModel
from models.establecimiento_model import EstablecimientoModel
from models.eventos_model import EventoModel
from os import environ
from dotenv import load_dotenv

#from flask_cors import CORS #instalar libreria

load_dotenv()

app = Flask(__name__)
api= Api(app)

app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DATABASE_URL')

conexion.init_app(app)

Migrate(app, conexion)

if __name__ == ("__main__"):
    app.run(debug=True)