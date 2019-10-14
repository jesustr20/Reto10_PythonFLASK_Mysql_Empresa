import pymysql
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Conexion:
    def __init__(self):
        self.db = pymysql.connect(os.getenv('DB_SERVER'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_NAME'))
        self.cursor = self.db.cursor()

    def ejecutar_sentencia(self, sql):
            self.cursor.execute(sql)
            return self.cursor
        
    def cerrar_conexion(self):
            self.db.close()
        
    def commit(self):
            self.db.commit()
            return
        
    def rollback(self):
            self.db.rollback()
            return
