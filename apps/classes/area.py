#AREA
from database.config import Conexion
from helper import helper

#TABLA AREA
class Area:
    def __init__(self, tipoArea=None):
        self.tipoArea = tipoArea

    
    def add_Area(self, area, app):
        try:    
            conn = Conexion()
            query = f'''
                INSERT INTO area(tipoArea)
                VALUES('{area.tipoArea}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agrego el area: {area.tipoA}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def listar_Area(self, app):
        listado_area = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM area
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_area.append({'id ':str(fila[0]), 'Cargo ': fila[1]})
            diccionario['Area'] = listado_area
            print(diccionario)
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def obtener_Area(self, app, id_area):
        listado_area = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM area WHERE id={id_area}
            '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            area = Area(fila[1])
            listado_area.append({'id ':str(fila[0]), 'Cargo ': area.tipoArea})
            diccionario['Area'] = listado_area
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def actualizar_Area(self, app, id_area, area):
        try:
            conn = Conexion()
            query = f'''
                UPDATE area
                SET tipoArea = '{id_area.tipoArea}'
                WHERE id = {id_area}
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            proces = 'Procesado'
            return helper.handler_response(app, 201, proces)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def eliminar_Area(self, app, id_area):
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM area WHERE id={id_area}
            '''
            cursor = conn.ejecutar_sentencia(query)
            conn.commit()
            eliminado = 'Eliminado...'
            return helper.handler_response(app, 201, eliminado)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()