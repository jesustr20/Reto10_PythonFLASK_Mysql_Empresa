import sys
sys.path.append('./.')
from flask import request
from apps.classes.users import Personal

personal = Personal()

def route(app):
    @app.route('/')
    def hello_world():
        return '<h1>Si funciona, Hola Mundo</h1>'
    
    @app.route('/personal/add', methods=['POST'])
    def personal_add():
        values = request.values
        personal.name = values.get('nombre')
        personal.last_name = values.get('apellido')
        personal.age = values.get('edad')
        personal.dni = values.get('dni')
        return personal.add_personal(personal, app)
    
    @app.route('/personal/todos', methods=['GET'])
    def allpersonal():
        return personal.listar_personal(app)

    #FOMAR 1, INTRODUCIR POR TECLADO DESDE EXPLORADOR
    @app.route('/personal/<int:id>')
    def personal_get(id):
        return personal.obtener_personal(app, id)
    
    #FORMA 2, OBTENER POR POSTMAN
    @app.route('/personal/buscar', methods=['GET'])
    def personal_buscar():
        values = request.values
        ide = values.get('id')
        return personal.obtener_personal(app, ide)

    @app.route('/personal/edit', methods=['PUT'])
    def personal_edit():
        values = request.values
        ide = values.get('id')
        personal.name = values.get('nombre')
        personal.last_name = values.get('apellido')
        personal.age = values.get('edad')
        personal.dni = values.get('dni')
        return personal.actualizar_personal(app,ide,personal)

    @app.route('/personal/delete', methods=['DELETE'])
    def personal_delete():
        values = request.values
        ide = values.get('id')
        return personal.eliminar_personal(app, ide)
    
    #Muestra todos los perosnales generales
    @app.route('/personal/cargo', methods=['GET'])
    def personal_cargo():
        return personal.cargo_personal(app)
    
    #Muestra datos por id
    @app.route('/personal/cargoid', methods=['GET'])
    def personal_cargoid():
        values = request.values
        ide = values.get('id')
        return personal.cargo_personalID(app,ide)