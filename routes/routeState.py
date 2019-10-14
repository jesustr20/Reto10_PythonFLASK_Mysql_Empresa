#ESTADO
import sys
sys.path.append('./.')
from flask import request
from apps.classes.state import State

estado = State()

def route(app):
    @app.route('/estado')
    def hola_estado():
        return 'Hola Estado'

    @app.route('/estado/add', methods=['POST'])
    def estado_add():
        values = request.values
        estado.tipoCargo = values.get('Estado')
        return estado.add_Estado(estado, app)
    
    @app.route('/Estado/todos', methods=['GET'])
    def estado_todos():
        return estado.listar_Estado(app)

    #FOMAR 1, INTRODUCIR POR TECLADO DESDE EXPLORADOR
    @app.route('/Estado/<int:id>')
    def estado_get(id):
        return estado.obtener_Estado(app, id)
    
    #FORMA 2, OBTENER POR POSTMAN
    @app.route('/Estado/buscar', methods=['GET'])
    def estado_buscar():
        values = request.values
        ide = values.get('id')
        return estado.obtener_Estado(app, ide)

    @app.route('/Estado/edit', methods=['PUT'])
    def estado_edit():
        values = request.values
        ide = values.get('id')
        estado.tipoCargo = values.get('cargo')
        return estado.actualizar_Estado(app,ide,estado)

    @app.route('/Estado/delete', methods=['DELETE'])
    def estado_delete():
        values = request.values
        ide = values.get('id')
        return estado.eliminar_estado(app, ide)
    

