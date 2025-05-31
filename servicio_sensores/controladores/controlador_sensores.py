# servicio_sensores/controladores/controlador_sensores.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from esquemas.esquema_sensor import DatosSensor
from repositorios.repositorio_datos_sensores import guardar_sensor, listar_sensores

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DatosSensor)
def crear_dato_sensor(datos: DatosSensor, db: Session = Depends(get_db)):
    """
    Recibe un JSON con:
    {
      "sensor_id": str,
      "humedad": float,
      "temperatura": float,
      "radiacion": float,
      "lluvia": float,
      "fecha": "YYYY-MM-DDTHH:MM:SS"
    }
    Guarda el dato en la base y devuelve el mismo objeto con el campo `id` generado.
    """
    return guardar_sensor(db, datos)

@router.get("/", response_model=list[DatosSensor])
def obtener_datos(db: Session = Depends(get_db)):
    """
    Devuelve la lista completa de datos de sensores almacenados.
    Cada elemento incluirá su campo `id` además de los demás campos.
    """
    return listar_sensores(db)
