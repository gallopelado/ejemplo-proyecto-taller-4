from flask import Flask, session

# Instancia principal
app = Flask(__name__)

# Guardar la clave secreta
app.secret_key = '123'

# login
from app.rutas.seguridad.login.login_routes import loginmod

# Vamos a importar lo necesario para los referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciudadmod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod

# Se registran los modulos de referenciales
ref = '/seguridad'
app.register_blueprint(loginmod, url_prefix=f"{ref}/login")
app.register_blueprint(ciudadmod, url_prefix=f"{ref}/ciudad")
app.register_blueprint(nacmod, url_prefix=f"{ref}/nacionalidad")

