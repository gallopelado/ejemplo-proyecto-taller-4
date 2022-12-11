import psycopg2
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonaModel:
    
    def listarTodos(self):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute('SELECT id, nombres, apellidos, ci, sexo FROM public.personas')
            items = cursor.fetchall()
            cursor.close()
            con.close()
            return items
        except (Exception, psycopg2.DatabaseError) as error:
            app.logger.error(f'Ha ocurrido un error al traer todas las personas, {error}')