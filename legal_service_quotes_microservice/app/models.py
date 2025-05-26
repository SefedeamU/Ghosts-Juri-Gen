from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Cotizacion(Base):
    __tablename__ = "cotizaciones"

    id = Column(Integer, primary_key=True, index=True)
    numero_cotizacion = Column(String(20), unique=True, index=True, nullable=False)
    nombre_cliente = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    tipo_servicio = Column(String(50), nullable=False)
    descripcion = Column(String(500), nullable=False)
    precio = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)