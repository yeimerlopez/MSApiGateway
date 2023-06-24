from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests
import re


from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager




# Agragamos las variables ´para hacer uso del framework y de los recurso cruzados
app = Flask(__name__)
cors = CORS(app)


app.config["JWT_SECRET_KEY"] = "super-secret" #Cambiar por el que sea conveniente
jwt = JWTManager(app)

# end point  iniciar seccion

@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url=dataConfig["url-backend-security"]+'/usuarios/validar'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60 * 60*24)
        access_token = create_access_token(identity=user,expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        return jsonify({"msg": "Bad username or password"}), 401




###################################Endpoints Facturas####################################################

@app.route("/facturas",methods=['GET'])
def getFacturas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/facturas'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/facturas",methods=['POST'])
def crearFactura():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/facturas'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@app.route("/facturas/<string:id>",methods=['GET'])
def getFactura(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/facturas/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/facturas/<string:id>",methods=['PUT'])
def modificarFactura(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/facturas/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)







@app.route("/facturas/<string:id>",methods=['DELETE'])
def eliminarFactura(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/facturas/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)



###########################################################################################
###################################Endpoints Clientes####################################################

@app.route("/clientes",methods=['GET'])
def getClientes():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/clientes'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/clientes",methods=['POST'])
def crearCliente():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/clientes'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@app.route("/clientes/<string:id>",methods=['GET'])
def getCliente(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/clientes/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)




@app.route("/clientes/<string:id>",methods=['PUT'])
def modificarCliente(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/clientes/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@app.route("/clientes/<string:id>",methods=['DELETE'])
def eliminarCliente(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/clientes/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)



###########################################################################################

###################################Endpoints Productos####################################################

@app.route("/productos",methods=['GET'])
def getProductos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/productos'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/productos",methods=['POST'])
def crearProducto():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/productos'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@app.route("/productos/<string:id>",methods=['GET'])
def getProducto(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/productos/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/productos/<string:id>",methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/productos/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)







@app.route("/productos/<string:id>",methods=['DELETE'])
def eliminarProducto(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/productos/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)



###########################################################################################

###################################Endpoints Ventas####################################################

@app.route("/ventas",methods=['GET'])
def getVentas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/ventas'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@app.route("/ventas",methods=['POST'])
def crearVenta():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/ventas'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@app.route("/ventas/<string:id>",methods=['GET'])
def getVenta(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/ventas/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)


@app.route("/ventas/<string:id>",methods=['PUT'])
def modificarVenta(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/ventas/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)







@app.route("/ventas/<string:id>",methods=['DELETE'])
def eliminarVenta(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-MS_facturacion"] + '/ventas/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)



###########################################################################################


##################################### Midleware  #########################
@app.before_request
def before_request_callback():
    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]
    if excludedRoutes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            tienePersmiso = validarPermiso(endPoint, request.method, usuario["rol"]["_id"])
            if not tienePersmiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401



def limpiarURL(url):
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url


def validarPermiso(endPoint,metodo,idRol):
    url = dataConfig["url-backend-security"]+"/permisos-roles/validar-permiso/rol/"+str(idRol)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url":endPoint,
        "metodo":metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso


###############################################################################################################






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