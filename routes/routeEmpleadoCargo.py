import sys
sys.path.append('./.')
from flask import request
from apps.classes.empleadoCargo import EmpleadoCargo

ec = EmpleadoCargo()

def route(app):
    @app.route('/ec')
    def hola_ec():
        return 'Hola Empleado Cargo'

    @app.route('/ec/add', methods=['POST'])
    def ec_add():
        values = request.values
        ec.idPersonal = values.get('idPersonal')
        ec.idArea = values.get('idArea')
        ec.idCargo = values.get('idCargo')
        ec.idEstado = values.get('idEstado')
        return ec.add_empleadoCargo(ec, app)
    
    @app.route('/ec/todos', methods=['GET'])
    def ec_todos():
        return ec.listar_empleadoCargo(app)

    #FOMAR 1, INTRODUCIR POR TECLADO DESDE EXPLORADOR
    @app.route('/ec/<int:id>')
    def ec_get(id):
        return ec.obtener_empleadoCargo(app, id)
    
    #FORMA 2, OBTENER POR POSTMAN
    @app.route('/ec/buscar', methods=['GET'])
    def ec_buscar():
        values = request.values
        ide = values.get('id')
        return ec.obtener_empleadoCargo(app, ide)

    @app.route('/ec/edit', methods=['PUT'])
    def ec_edit():
        values = request.values
        ide = values.get('id')
        ec.idPersonal = values.get('idPersonal')
        ec.idArea = values.get('idArea')
        ec.idCargo = values.get('idCargo')
        ec.idEstado = values.get('idEstado')
        return ec.actualizar_empleadoCargo(app,ide,ec)

    @app.route('/ec/delete', methods=['DELETE'])
    def ec_delete():
        values = request.values
        ide = values.get('id')
        return ec.eliminar_cargo(app, ide)
    
