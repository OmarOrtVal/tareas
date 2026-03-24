from src.models.TareaModel import TareaModel 

class TareasController:
    def __init__(self):
        self.model=TareaModel()
    
    def obtener_lista(self,id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva(self,id_usuario,titulo,desc,prio,clas):
        if not titulo:
            return False,"El titulo es obligatorio"
        
        self.mode.crear(id_usuario,titulo,desc,prio,clas)
        return True, "Tarea guardada"