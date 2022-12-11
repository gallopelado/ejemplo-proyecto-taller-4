from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from markupsafe import escape
from app.modelos.referenciales.personas.PersonaModel import PersonaModel

permod = Blueprint('persona', __name__, template_folder="templates")
persona_model = PersonaModel()

@permod.route('/')
def index():
    return render_template('persona/index.html')

# REST Endpoints
@permod.route('/listar')
def listar():
    items = persona_model.listarTodos()
    lista_personas = []
    for item in items:
        """ sexo = ''
        if item[4] == 'F':
            sexo = 'FEMENINO'
        elif item[4] == 'M':
            sexo = 'MASCULINO'
        else:
            sexo = 'INDETERMINADO' """
            
        lista_personas.append({
            'id': item[0], 'nombres': item[1], 'apellidos': item[2], 'ci': item[3]
            , 'sexo': 'FEMENINO' if item[4] == 'F' else 'MASCULINO' if item[4] == 'M' else 'INDETERMINADO'
        })
    return jsonify(lista_personas)