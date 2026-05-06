from .databaseModel import Database
from datetime import datetime

class TareaModel:
    def __init__(self):
        self.db = Database()
    
    def listar_por_usuario(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *, 
                DATE_FORMAT(fecha_creacion, '%Y-%m-%d %H:%i:%s') as fecha_creacion_formateada 
                FROM tareas 
                WHERE id_usuario = %s 
                ORDER BY fecha_limite ASC"""
        cursor.execute(query, (id_usuario,))
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    
    def crear(self, id_usuario, titulo, descripcion, prioridad, clasificacion, 
            estado, fecha_limite=None, hora_limite=None):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        fecha_creacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = """INSERT INTO tareas(id_usuario, titulo, descripcion, prioridad, 
                clasificacion, estado, fecha_limite, hora_limite, fecha_creacion)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (id_usuario, titulo, descripcion, prioridad, 
                            clasificacion, estado, fecha_limite, hora_limite, fecha_creacion))
        conn.commit()
        conn.close()
    
    def eliminar(self, id_tarea):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM tareas WHERE id_tarea = %s"
        cursor.execute(query, (id_tarea,))
        conn.commit()
        conn.close()