import mysql.connector 
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def get_connection(self):
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="gestor_tareas"
        )