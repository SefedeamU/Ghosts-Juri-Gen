from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def calcular_precio(tipo_servicio: str) -> float:
    precios = {
        "Constitución de empresa": 1500,
        "Defensa laboral": 2000,
        "Consultoría tributaria": 800
    }
    return precios.get(tipo_servicio, 0)

def crear_cotizacion(db: Session, cotizacion: schemas.CotizacionCreate, numero_cotizacion: str, precio: float):
    db_cotizacion = models.Cotizacion(
        numero_cotizacion=numero_cotizacion,
        nombre_cliente=cotizacion.nombre_cliente,
        email=cotizacion.email,
        tipo_servicio=cotizacion.tipo_servicio,
        descripcion=cotizacion.descripcion,
        precio=precio,
        fecha=datetime.utcnow()
    )
    db.add(db_cotizacion)
    db.commit()
    db.refresh(db_cotizacion)
    return db_cotizacion

def listar_cotizaciones(db: Session):
    return db.query(models.Cotizacion).all()

def obtener_cotizacion(db: Session, cotizacion_id: int):
    return db.query(models.Cotizacion).filter(models.Cotizacion.id == cotizacion_id).first()

def actualizar_cotizacion(db: Session, cotizacion_id: int, cotizacion_update: schemas.CotizacionCreate):
    cotizacion = db.query(models.Cotizacion).filter(models.Cotizacion.id == cotizacion_id).first()
    if cotizacion:
        cotizacion.nombre_cliente = cotizacion_update.nombre_cliente
        cotizacion.email = cotizacion_update.email
        cotizacion.tipo_servicio = cotizacion_update.tipo_servicio
        cotizacion.descripcion = cotizacion_update.descripcion
        cotizacion.precio = calcular_precio(cotizacion_update.tipo_servicio)
        db.commit()
        db.refresh(cotizacion)
    return cotizacion

def borrar_cotizacion(db: Session, cotizacion_id: int):
    cotizacion = db.query(models.Cotizacion).filter(models.Cotizacion.id == cotizacion_id).first()
    if cotizacion:
        db.delete(cotizacion)
        db.commit()
    return cotizacion