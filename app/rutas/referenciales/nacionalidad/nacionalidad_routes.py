from flask import Blueprint, render_template

# Se crea el módulo para Blueprint
nacmod = Blueprint("nacionalidad", __name__, template_folder="templates")

# Los endpoints
@nacmod.route('/')
def index():
    return render_template('nacionalidad/index.html')