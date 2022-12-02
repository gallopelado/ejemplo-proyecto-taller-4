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
            
    def traerPorId(self, id):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT id, descripcion FROM public.nacionalidades WHERE id=%s", (id,))
            item = cursor.fetchone()
            cursor.close()
            con.close()
            return item
        except:
            app.logger.error('Ha ocurrido un error al traer una nacionalidad')
            
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
            
    def actualizar(self, id, descripcion):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("UPDATE public.nacionalidades SET descripcion=%s WHERE id=%s", (descripcion, id,))
            # Aqui se confirma la transaccion SQL
            con.commit()
            cursor.close()
            con.close()
            return True
        except:
            app.logger.error('Ha ocurrido un error al ACTUALIZAR')
            
    def eliminar(self, id):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("DELETE FROM public.nacionalidades WHERE id=%s", (id,))
            # Aqui se confirma la transaccion SQL
            con.commit()
            cursor.close()
            con.close()
            return True
        except:
            app.logger.error('Ha ocurrido un error al ELIMINAR')