# servicio_sensores/main.py

from fastapi import FastAPI
from controladores.controlador_sensores import router as sensor_router
from config.database import Base, engine

app = FastAPI(title="Servicio de Sensores")

# Crear tablas en PostgreSQL (solo la primera vez)
Base.metadata.create_all(bind=engine)

app.include_router(sensor_router, prefix="/sensores", tags=["Sensores"])
