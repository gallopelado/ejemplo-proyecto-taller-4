from flask import Flask, render_template

app = Flask(__name__)

#from app import rutas
# Vamos a importar lo necesario para los referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciudadmod

# Se registran los modulos de referenciales
# Versión corta
app.register_blueprint(ciudadmod, url_prefix="/ciudad")

# Versión larga
#app.register_blueprint(rutas.ciudad.ciudad_routes.ciudadmod, url_prefix="/ciudad")