from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from routes import routeUsers, route_error, routePosition, routeArea, routeState, routeEmpleadoCargo

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#Ruta Usuarios
routeUsers.route(app)
#RUTA QUE VERIFICA SI EXISTE O NO LA PAGINA
route_error.error_handler(app)
#RUTA DEL CARGO
routePosition.route(app)
#RUTA DE LAS AREAS
routeArea.route(app)
#RUTA DEL ESTADO
routeState.route(app)
#RUTA PARA LA INFO DE EMPLEADO CARGO
routeEmpleadoCargo.route(app)

if __name__ == '__main__':
    app.run()