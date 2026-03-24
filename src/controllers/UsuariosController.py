from src.mode.UserModel import UsuarioModel 
from src.models.schemasModel import UsuariosSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, email,passwrod):
        try:
            nuevo_usuario=UsuariosSchema(nombre=nombre, email=email,password=passwrod)
            sucess=self.model.registrar(nuevo_usuario)
            return sucess, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']