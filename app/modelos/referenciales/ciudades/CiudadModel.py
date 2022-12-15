import psycopg2
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CiudadModel:
    
    def listarTodos(self):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT id, descripcion FROM public.ciudades")
            items = cursor.fetchall()
            cursor.close()
            con.close()
            return items
        except:
            app.logger.error('Ha ocurrido un error al listar ciudades')
            
    def traerPorId(self, id):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("SELECT id, descripcion FROM public.ciudades WHERE id=%s", (id,))
            item = cursor.fetchone()
            cursor.close()
            con.close()
            return item
        except:
            app.logger.error('Ha ocurrido un error al traer una ciudad')
            
    def agregar(self, descripcion):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("INSERT INTO public.ciudades(descripcion) VALUES(%s)", (descripcion,))
            # Aqui se confirma la transaccion SQL
            con.commit()
            cursor.close()
            con.close()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            app.logger.error(f'Ha ocurrido un error al INSERTAR, mensaje= {error}')
            
    def actualizar(self, id, descripcion):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("UPDATE public.ciudades SET descripcion=%s WHERE id=%s", (descripcion, id,))
            # Aqui se confirma la transaccion SQL
            con.commit()
            cursor.close()
            con.close()
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            app.logger.error('Ha ocurrido un error al ACTUALIZAR, mensaje= {error}')
            
    def eliminar(self, id):
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cursor = con.cursor()
            cursor.execute("DELETE FROM public.ciudades WHERE id=%s", (id,))
            # Aqui se confirma la transaccion SQL
            con.commit()
            cursor.close()
            con.close()
            return True
        except:
            app.logger.error('Ha ocurrido un error al ELIMINAR')