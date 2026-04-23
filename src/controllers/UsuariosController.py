from models.UsuariosModel import UsuarioModel 
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        # Tu código de inicialización aquí
        pass
    
    def login(self, email, password):
        """Método para autenticar usuario"""
        # Aquí va tu lógica de autenticación
        # Por ejemplo, validación simple o consulta a base de datos
        
        # Ejemplo con validación simple:
        if email == "admin@gmail.com" and password == "1234":
            user = {
                "email": email,
                "name": "Administrador",
                "role": "admin"
            }
            return user, "Login exitoso"
        else:
            return None, "Correo o contraseña incorrectos"