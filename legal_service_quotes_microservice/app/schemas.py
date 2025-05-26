from pydantic import BaseModel, EmailStr
from datetime import datetime

class CotizacionCreate(BaseModel):
    nombre_cliente: str
    email: EmailStr
    tipo_servicio: str
    descripcion: str

class CotizacionResponse(BaseModel):
    id: int
    numero_cotizacion: str
    precio: float
    fecha: datetime
    nombre_cliente: str
    email: EmailStr
    tipo_servicio: str
    descripcion: str

    class Config:
        from_attributes = True