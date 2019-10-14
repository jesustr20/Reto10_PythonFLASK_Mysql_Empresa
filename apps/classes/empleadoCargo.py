#ESTADO_CARGO
#CARGO
from database.config import Conexion
from helper import helper

#TABLA Empleado CARGO
class EmpleadoCargo:
    def __init__(self, idPersonal=None, idArea=None, idCargo=None, idEstado=None):
        self.idPersonal = idPersonal
        self.idArea = idArea
        self.idCargo = idCargo
        self.idEstado = idEstado
    
    def add_empleadoCargo(self, ec, app):
        try:    
            conn = Conexion()
            query = f'''
                INSERT INTO empleado_cargo(id_personal, id_area, id_cargo, id_estado)
                VALUES('{ec.idPersonal}','{ec.idArea}','{ec.idCargo}','{ec.idEstado}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agrego el cargo: idPersonal: {ec.idPersonal}, idArea: {ec.idArea}, idCargo: {ec.idCargo}, idEstado: {ec.idEstado}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def listar_empleadoCargo(self, app):
        listado_ec = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM empleado_cargo
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_ec.append({'id ':str(fila[0]), 'idPersonal ': fila[1], 'idArea ':fila[2], 'idCargo ':fila[3], 'idEstado ':fila[4]})
            diccionario['Empleado Cargo'] = listado_ec
            print(diccionario)
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def obtener_empleadoCargo(self, app, id_ec):
        listado_ec = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM empleado_cargo WHERE id={id_ec}
            '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            ec = EmpleadoCargo(fila[1], fila[2],fila[3],fila[4])
            listado_ec.append({'id ':str(fila[0]), 'idPersonal ': ec.idPersonal, 'idArea ':ec.idArea, 'idCargo ':ec.idCargo, 'idEstado ':ec.idEstado})
            diccionario['Empleado Cargo'] = listado_ec
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def actualizar_empleadoCargo(self, app, id_ec, ec):
        try:
            conn = Conexion()
            query = f'''
                UPDATE empleado_cargo
                SET id_personal = '{id_ec.idPersonal}',
                    id_area = '{id_ec.idArea}',
                    id_cargo = '{id_ec.idCargo}',
                    id_estado = '{id_ec.idEstado}'
                WHERE id = {id_ec}
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
    
    def eliminar_cargo(self, app, id_ec):
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM empleado_cargo WHERE id={id_ec}
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