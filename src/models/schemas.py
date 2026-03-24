from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date,time

class UsuarioSchema(BaseModel):
    nombre: str=Field(min_length=3, mas_length=100)
    email: EmailStr
    password: str = Field (min_length=8)
    
class TareaSchema(BaseModel):
    titulo: str = Field (min_length=1 , max_lenght=200)
    descripcion: Optional[str]=None
    prioridad: str= "media"
    clasificion: str ="personal"