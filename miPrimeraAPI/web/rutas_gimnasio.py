from flask import request, session
import json
import decimal
from __main__ import app
import controlador_gimnasio

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/gimnasio",methods=["GET"])
def gimnasio():
    gimnasio,code= controlador_gimnasio.obtener_gimnasio()
    return json.dumps(gimnasio, cls = Encoder),code

@app.route("/gimnasio/<id>",methods=["GET"])
def gimnasio_por_id(id):
    gimnasio,code = controlador_gimnasio.obtener_gimnasio_por_id(id)
    return json.dumps(gimnasio, cls = Encoder),code

@app.route("/gimnasio",methods=["POST"])
def guardar_gimnasio():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        gimnasio_json = request.json
        ret,code=controlador_gimnasio.insertar_gimnasio(gimnasio_json["nombre"], gimnasio_json["descripcion"], float(gimnasio_json["precio"]), gimnasio_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/gimnasio/<id>", methods=["DELETE"])
def eliminar_gimnasio(id):
    ret,code=controlador_gimnasio.eliminar_gimnasio(id)
    return json.dumps(ret), code

@app.route("/gimnasio", methods=["PUT"])
def actualizar_gimnasio():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        gimnasio_json = request.json
        ret,code=controlador_gimnasio.actualizar_gimnasio(gimnasio_json["id"],gimnasio_json["nombre"], gimnasio_json["descripcion"], float(gimnasio_json["precio"]),gimnasio_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code