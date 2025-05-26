from pydantic import BaseModel, EmailStr
from datetime import datetime

class AnalisisRequest(BaseModel):
    numero_cotizacion: str
    precio: float
    fecha: datetime
    nombre_cliente: str
    email: EmailStr
    tipo_servicio: str
    descripcion: str

class AnalisisResponse(BaseModel):
    complejidad: str
    ajuste_precio: int
    servicios_adicionales: list[str]
    propuesta_texto: str