from database.config import Conexion
from helper import helper

class Personal:
    def __init__(self, name=None, last_name=None, age=None, dni=None):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.dni = dni

    def add_personal(self, personal, app):
        try:    
            conn = Conexion()
            query = f'''
                INSERT INTO personal(nombre, apellido, edad, dni)
                VALUES('{personal.name}','{personal.last_name}','{personal.age}','{personal.dni}')
            '''
            conn.ejecutar_sentencia(query)
            conn.commit()
            message = f'''Se agrego el usuario: {personal.name}, {personal.last_name}'''
            return helper.handler_response(app, 201, message)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def listar_personal(self, app):
        listado_personal = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM personal
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                listado_personal.append({'id ':str(fila[0]), 'Nombre ': fila[1], 'Apellido ':fila[2],'Edad: ':fila[3], 'Dni: ':fila[4]})
            diccionario['personal'] = listado_personal
            print(diccionario)
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def obtener_personal(self, app, id_personal):
        listado_personal = []
        diccionario={}
        try:
            conn = Conexion()
            query = f'''
                SELECT * FROM personal WHERE id={id_personal}
            '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            personal = Personal(fila[1], fila[2], fila[3], fila[4])
            listado_personal.append({'id ':str(fila[0]), 'Nombre ': personal.name, 'Apellido ':personal.last_name,'Edad ':personal.age, 'Dni ':personal.dni})
            diccionario['personal'] = listado_personal
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
    
    def actualizar_personal(self, app, id_personal, personal):
        try:
            conn = Conexion()
            query = f'''
                UPDATE personal
                SET nombre = '{personal.name}',
                    apellido = '{personal.last_name}',
                    edad = '{personal.age}',
                    dni = '{personal.dni}'
                WHERE id = {id_personal}
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
    

    def eliminar_personal(self, app, id_personal):
        try:
            conn = Conexion()
            query = f'''
                DELETE FROM personal WHERE id={id_personal}
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
    
    #TABLA QUE MOSTRARA DATOS DEL PERSONAL
    def cargo_personal(self, app):
        listado_personal = []
        diccionario={}
        try:
            conn = Conexion()            
            query = f'''
                Select e.id, p.nombre, p.apellido, a.tipoArea, c.tipoCargo,c.nivel, l.tipoEstado
                from empleado_cargo as e
                inner join personal p on e.id_personal = p.id
                inner join area a on e.id_area = a.id
                inner join cargo c on e.id_cargo = c.id
                inner join estado l on e.id_estado = l.id
            '''
            cursor = conn.ejecutar_sentencia(query)
            filas = cursor.fetchall()
            for fila in filas:
                dicc = ({'id ':str(fila[0]), 'Nombre ': fila[1], 'Apellido ':fila[2],'Area ':fila[3], 'Cargo ':fila[4], 'Nivel ':fila[5],'Estado ':fila[6] })
                listado_personal.append(dicc)
            diccionario[''] =listado_personal
            print(diccionario)
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()
        
    def cargo_personalID(self, app, ide):
        listado_personal = []
        diccionario={}
        try:
            conn = Conexion()            
            query = f'''
                Select e.id, p.nombre, p.apellido, a.tipoArea, c.tipoCargo, l.tipoEstado
                from empleado_cargo as e
                inner join personal p on e.id_personal = p.id
                inner join area a on e.id_area = a.id
                inner join cargo c on e.id_cargo = c.id
                inner join estado l on e.id_estado = l.id
                Where e.id={ide}
            '''
            cursor = conn.ejecutar_sentencia(query)
            fila = cursor.fetchone()
            dicc = ({'id ':str(fila[0]), 'Nombre ': fila[1], 'Apellido ':fila[2],'Area ':fila[3], 'Cargo ':fila[4], 'Estado ':fila[5]})
            listado_personal.append(dicc)
            diccionario[''] =listado_personal
            print(diccionario)
            return helper.handler_response(app, 201, diccionario)
        except Exception as e:
            raise
            print(e)
        finally:
            conn.cerrar_conexion()

#cargar = Personal("","","","")
#cargar.cargo_personalID(2)

