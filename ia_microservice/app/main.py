from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import AnalisisRequest, AnalisisResponse
from app.ia_client import analizar_con_ia

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analizar", response_model=AnalisisResponse)
def analizar(request: AnalisisRequest):
    resultado = analizar_con_ia(
        numero_cotizacion=request.numero_cotizacion,
        precio=request.precio,
        fecha=request.fecha,
        nombre_cliente=request.nombre_cliente,
        email=request.email,
        tipo_servicio=request.tipo_servicio,
        descripcion=request.descripcion
    )
    return resultado