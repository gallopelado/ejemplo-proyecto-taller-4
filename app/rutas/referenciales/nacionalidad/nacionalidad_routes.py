from flask import Blueprint, render_template
from app.modelos.referenciales.nacionalidades.NacionalidadModel import NacionalidadModel

# Se crea el módulo para Blueprint
nacmod = Blueprint("nacionalidad", __name__, template_folder="templates")
nac_model = NacionalidadModel()

# Los endpoints
@nacmod.route('/')
def index():
    items = nac_model.listarTodos()
    print(items)
    return render_template('nacionalidad/index.html', items=items)