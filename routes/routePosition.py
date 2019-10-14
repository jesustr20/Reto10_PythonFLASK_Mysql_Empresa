import sys
sys.path.append('./.')
from flask import request
from apps.classes.position import Position

cargo = Position()

def route(app):
    @app.route('/position')
    def hola_cargo():
        return 'Hola cargo'

    @app.route('/position/add', methods=['POST'])
    def position_add():
        values = request.values
        cargo.tipoCargo = values.get('Cargo')
        cargo.nivel = values.get('Nivel')
        return cargo.add_Cargo(cargo, app)
    
    @app.route('/position/todos', methods=['GET'])
    def cargo_todos():
        return cargo.listar_Cargo(app)

    #FOMAR 1, INTRODUCIR POR TECLADO DESDE EXPLORADOR
    @app.route('/position/<int:id>')
    def cargo_get(id):
        return cargo.obtener_cargo(app, id)
    
    #FORMA 2, OBTENER POR POSTMAN
    @app.route('/position/buscar', methods=['GET'])
    def cargo_buscar():
        values = request.values
        ide = values.get('id')
        return cargo.obtener_cargo(app, ide)

    @app.route('/position/edit', methods=['PUT'])
    def cargo_edit():
        values = request.values
        ide = values.get('id')
        cargo.tipoCargo = values.get('cargo')
        cargo.nivel = values.get('nivel')
        return cargo.actualizar_cargo(app,ide,cargo)

    @app.route('/position/delete', methods=['DELETE'])
    def cargo_delete():
        values = request.values
        ide = values.get('id')
        return cargo.eliminar_cargo(app, ide)
    
