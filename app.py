from flask import Flask
from flask_restful import Api
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
#from flask_cors import CORS #instalar libreria

load_dotenv()

app = Flask(__name__)
api= Api(app)

app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DATABASE_URL')

if __name__ == ("__main__"):
    app.run(debug=True)