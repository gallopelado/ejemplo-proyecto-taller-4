from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from markupsafe import escape
from app.modelos.referenciales.ciudades.CiudadModel import CiudadModel

# Se modularizan las vistas de ciudades.
ciudadmod = Blueprint("ciudad", __name__, template_folder="templates")
ciu_model = CiudadModel()

# Lugarcito de los endpoints
@ciudadmod.route('/')
def index():
    #return "Hola mundo en ciudad"
    return render_template('ciudad/index.html')

# APIS REST
@ciudadmod.route('/get_ciudades', methods=['GET'])
def get_ciudades():
    items = ciu_model.listarTodos()
    lista_ciudades = []
    for item in items:
        lista_ciudades.append({"id": item[0], "descripcion": item[1]})
    return jsonify(lista_ciudades)

@ciudadmod.route('/get_ciudad_id/<id>', methods=['GET'])
def get_ciudad_id(id):
    item = ciu_model.traerPorId(escape(id))
    data = {
        "id": item[0], "descripcion": item[1]
    }
    return jsonify(data)

@ciudadmod.route('/agregar_ciudad', methods=['POST'])
def agregar_ciudad():
    print(request.json['descripcion'])
    # hacer las validaciones
    descripcion = request.json['descripcion']
    res = ciu_model.agregar(descripcion)
    if res:
        return jsonify({'estado': res, 'mensaje': 'se guardo exitosamente'})
    return jsonify({'estado': 'error', 'mensaje': 'hendy'})



