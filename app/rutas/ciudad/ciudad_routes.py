from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

# Se modularizan las vistas de ciudades.
ciudadmod = Blueprint("ciudad", __name__, template_folder="templates")

# Lugarcito de los endpoints
@ciudadmod.route('/')
def index():
    #return "Hola mundo en ciudad"
    return render_template('ciudad/index.html')

@ciudadmod.route('/listar_todos')
def listar_todos():
    return 'Aqui voy a listar mis ciudades'



