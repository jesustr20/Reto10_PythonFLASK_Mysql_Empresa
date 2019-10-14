#CARGO
from database.config import Conexion
from helper import helper

#TABLA CARGO
class Position:
    def __init__(self, tipoCargo=None, nivel=None):
        self.tipoCargo = tipoCargo
        self.nivel = nivel
    
    def add_Cargo(self, cargo, app):
        try:    
            conn = Conexion()
            query = f'''
                INSERT INTO cargo(tipoCargo, nivel)
                VALUES('{cargo.tipoCargo}','{cargo.nivel}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agrego el cargo: {cargo.tipoCargo}, {cargo.nivel}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def listar_Cargo(self, app):
        listado_cargo = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM cargo
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_cargo.append({'id ':str(fila[0]), 'Cargo ': fila[1], 'Nivel ':fila[2]})
            diccionario['Cargo'] = listado_cargo
            print(diccionario)
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def obtener_cargo(self, app, id_cargo):
        listado_cargo = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM cargo WHERE id={id_cargo}
            '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            cargo = Position(fila[1], fila[2])
            listado_cargo.append({'id ':str(fila[0]), 'Cargo ': cargo.tipoCargo, 'Nivel ':cargo.nivel})
            diccionario['Cargo'] = listado_cargo
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def actualizar_cargo(self, app, id_cargo, cargo):
        try:
            conn = Conexion()
            query = f'''
                UPDATE cargo
                SET nombre = '{id_cargo.tipoCargo}',
                    apellido = '{id_cargo.nivel}'
                WHERE id = {id_cargo}
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
    
    def eliminar_cargo(self, app, id_cargo):
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM cargo WHERE id={id_cargo}
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