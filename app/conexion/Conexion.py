import psycopg2

class Conexion:
    
    def __init__(self):
        self.__con = psycopg2.connect("dbname=prueba user=juandba host=localhost password=admin")
        
    def getConexion(self):
        return self.__con