import sys
sys.path.append('./.')
from flask import request
from apps.classes.area import Area

area = Area()

def route(app):
    @app.route('/area')
    def hola_area():
        return 'Hola area'

    @app.route('/area/add', methods=['POST'])
    def area_add():
        values = request.values
        area.tipoCargo = values.get('Area')
        return area.add_Area(area, app)
    
    @app.route('/area/todos', methods=['GET'])
    def area_todos():
        return area.listar_Area(app)

    #FOMAR 1, INTRODUCIR POR TECLADO DESDE EXPLORADOR
    @app.route('/area/<int:id>')
    def area_get(id):
        return area.obtener_Area(app, id)
    
    #FORMA 2, OBTENER POR POSTMAN
    @app.route('/area/buscar', methods=['GET'])
    def area_buscar():
        values = request.values
        ide = values.get('id')
        return area.obtener_Area(app, ide)

    @app.route('/area/edit', methods=['PUT'])
    def area_edit():
        values = request.values
        ide = values.get('id')
        area.tipoCargo = values.get('Area')
        return area.actualizar_Area(app,ide,area)

    @app.route('/area/delete', methods=['DELETE'])
    def area_delete():
        values = request.values
        ide = values.get('id')
        return area.eliminar_Area(app, ide)
    
