from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests



# Agragamos las variables ´para hacer uso del framework y de los recurso cruzados
app = Flask(__name__)
cors = CORS(app)


# permite ver si el servidor se esta inicializando o no

@app.route("/",methods=['GET'])
def test():
     json = {}
     json["message"]="Server running ..."
     return jsonify(json)

#Funcion para poder leer el archivo de congiguracion


def loadFileConfig():
     with open('config.json') as f:
        data = json.load(f)
     return data


if __name__=='__main__':
     dataConfig = loadFileConfig()
     print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
     serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])