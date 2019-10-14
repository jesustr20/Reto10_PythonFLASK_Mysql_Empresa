#ESTADO
from database.config import Conexion
from helper import helper

#TABLA ESTAD0
class State:
    def __init__(self, tipoEstado=None):
        self.tipoEstado = tipoEstado
    
    def add_Estado(self, estado, app):
        try:    
            conn = Conexion()
            query = f'''
                INSERT INTO cargo(tipoCargo, nivel)
                VALUES('{estado.tipoEstado}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agrego el Estado: {estado.tipoEstado}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def listar_Estado(self, app):
        listado_cargo = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM estado
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_cargo.append({'id ':str(fila[0]), 'Estad ': fila[1]})
            diccionario['Estado'] = listado_cargo
            print(diccionario)
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def obtener_Estado(self, app, id_estado):
        listado_estado = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM estado WHERE id={id_estado}
            '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            estado = State(fila[1])
            listado_estado.append({'id ':str(fila[0]), 'Estado ': estado.tipoEstado})
            diccionario['Estado'] = listado_estado
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def actualizar_Estado(self, app, id_estado, estado):
        try:
            conn = Conexion()
            query = f'''
                UPDATE estado
                SET nombre = '{id_estado.tipoEstado}'
                WHERE id = {id_estado}
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
    
    def eliminar_estado(self, app, id_estado):
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM estado WHERE id={id_estado}
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