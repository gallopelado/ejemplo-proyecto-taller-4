from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
from markupsafe import escape
from app.modelos.referenciales.nacionalidades.NacionalidadModel import NacionalidadModel

# Se crea el módulo para Blueprint
nacmod = Blueprint("nacionalidad", __name__, template_folder="templates")
nac_model = NacionalidadModel()

@nacmod.before_request
def before_request():
    if 'user' not in session:
        return redirect(url_for('login.index'))

# Los endpoints de formularios
@nacmod.route('/')
def index():
    items = nac_model.listarTodos()
    return render_template('nacionalidad/index.html', items=items)

@nacmod.route('/frm_nacionalidad')
def frm_nacionalidad():
    id = request.args.get('id')
    descripcion = request.args.get('descripcion')
    return render_template('nacionalidad/frm_nacionalidad.html', nac={ 'id': id, 'descripcion': descripcion })

@nacmod.route('/guardar', methods=['POST'])
def guardar_nacionalidad():
    descripcion = request.form['txt_nacionalidad']
    id =  request.form['txt_id_nacionalidad']
    if descripcion is None or descripcion.strip() == '':
        print('Ups, estaba vacio')
        return redirect(url_for('nacionalidad.frm_nacionalidad'))
    # Si hay algo en id es editar
    if id:
        nac_model.actualizar(id, descripcion.upper())
        print('Genial--Actualizado')
    # Si NO hay algo en id es agregar
    else:
        nac_model.agregar(descripcion.upper())
        print('Genial')
    return redirect(url_for('nacionalidad.index'))


@nacmod.route('/eliminar/', methods=['GET'])
def eliminar_nacionalidad():
    id = request.args.get('id')
    nac_model.eliminar(id)
    return redirect(url_for('nacionalidad.index'))

@nacmod.route('/get_nacionalidad_id/<id>', methods=['GET'])
def get_nacionalidad(id):
    item = nac_model.traerPorId(escape(id))
    data = {
        "id": item[0], "nacionalidad": item[1]
    }
    return jsonify(data)
