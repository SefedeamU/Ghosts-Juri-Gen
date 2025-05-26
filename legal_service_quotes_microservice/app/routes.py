from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db
from datetime import datetime
import uuid

router = APIRouter()

def generar_numero_cotizacion() -> str:
    anio = datetime.now().year
    numero = str(uuid.uuid4().int)[:4]
    return f"COT-{anio}-{numero}"

@router.post("/cotizaciones", response_model=schemas.CotizacionResponse)
def crear_cotizacion(cotizacion: schemas.CotizacionCreate, db: Session = Depends(get_db)):
    precio = crud.calcular_precio(cotizacion.tipo_servicio)
    if precio == 0:
        raise HTTPException(status_code=400, detail="Tipo de servicio no válido")
    numero_cotizacion = generar_numero_cotizacion()
    db_cotizacion = crud.crear_cotizacion(db, cotizacion, numero_cotizacion, precio)
    return db_cotizacion

@router.get("/cotizaciones", response_model=list[schemas.CotizacionResponse])
def listar_cotizaciones(db: Session = Depends(get_db)):
    return crud.listar_cotizaciones(db)

@router.get("/cotizaciones/{cotizacion_id}", response_model=schemas.CotizacionResponse)
def obtener_cotizacion(cotizacion_id: int, db: Session = Depends(get_db)):
    cotizacion = crud.obtener_cotizacion(db, cotizacion_id)
    if not cotizacion:
        raise HTTPException(status_code=404, detail="Cotización no encontrada")
    return cotizacion

@router.put("/cotizaciones/{cotizacion_id}", response_model=schemas.CotizacionResponse)
def actualizar_cotizacion(cotizacion_id: int, cotizacion_update: schemas.CotizacionCreate, db: Session = Depends(get_db)):
    cotizacion = crud.actualizar_cotizacion(db, cotizacion_id, cotizacion_update)
    if not cotizacion:
        raise HTTPException(status_code=404, detail="Cotización no encontrada")
    return cotizacion

@router.delete("/cotizaciones/{cotizacion_id}")
def borrar_cotizacion(cotizacion_id: int, db: Session = Depends(get_db)):
    cotizacion = crud.borrar_cotizacion(db, cotizacion_id)
    if not cotizacion:
        raise HTTPException(status_code=404, detail="Cotización no encontrada")
    return {"detail": "Cotización eliminada"}