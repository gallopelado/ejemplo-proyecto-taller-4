from flask import Blueprint, render_template, request, redirect, url_for
from app.modelos.referenciales.nacionalidades.NacionalidadModel import NacionalidadModel

# Se crea el módulo para Blueprint
nacmod = Blueprint("nacionalidad", __name__, template_folder="templates")
nac_model = NacionalidadModel()

# Los endpoints de formularios
@nacmod.route('/')
def index():
    items = nac_model.listarTodos()
    print(items)
    return render_template('nacionalidad/index.html', items=items)

@nacmod.route('/frm_nacionalidad')
def frm_nacionalidad():
    return render_template('nacionalidad/frm_nacionalidad.html')

@nacmod.route('/guardar', methods=['POST'])
def guardar_nacionalidad():
    descripcion = request.form['txt_nacionalidad']
    if descripcion is None or descripcion.strip() == '':
        print('Ups, estaba vacio')
        return redirect(url_for('nacionalidad.frm_nacionalidad'))
    nac_model.agregar(descripcion.upper())
    print('Genial')
    return redirect(url_for('nacionalidad.index'))
