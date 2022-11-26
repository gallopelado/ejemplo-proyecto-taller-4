from flask import Flask, render_template

app = Flask(__name__)

#from app import rutas
# Vamos a importar lo necesario para los referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciudadmod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod

# Se registran los modulos de referenciales
# Versión corta
app.register_blueprint(ciudadmod, url_prefix="/ciudad")
app.register_blueprint(nacmod, url_prefix="/nacionalidad")

# Versión larga
#app.register_blueprint(rutas.ciudad.ciudad_routes.ciudadmod, url_prefix="/ciudad")