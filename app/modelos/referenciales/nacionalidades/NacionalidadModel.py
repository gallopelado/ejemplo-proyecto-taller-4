from flask import current_app as app
from app.conexion.Conexion import Conexion

class NacionalidadModel:
    
    def listarTodos(self):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT id, descripcion FROM public.nacionalidades")
            items = cursor.fetchall()
            cursor.close()
            con.close()
            return items
        except:
            app.logger.error('Ha ocurrido un error al listar nacionalidades')
            
    def agregar(self, descripcion):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("INSERT INTO public.nacionalidades(descripcion) VALUES(%s)", (descripcion,))
            # Aqui se confirma la transaccion SQL
            con.commit()
            cursor.close()
            con.close()
            return True
        except:
            app.logger.error('Ha ocurrido un error al INSERTAR')