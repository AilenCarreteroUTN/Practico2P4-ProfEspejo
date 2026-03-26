from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Simulación de la base de datos.
class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=3, example="Homero Simpsons")
    email: EmailStr = Field(..., example="homerosimpsons@springfield.com") 
    cuil: int = Field(..., ge=0, example=123456789)
    activo: bool = True

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3)
    email: Optional[EmailStr] = None
    cuil: Optional[int] = Field(None, ge=0)
    activo: Optional[bool] = None

class ClienteRead(ClienteBase):
    id: int