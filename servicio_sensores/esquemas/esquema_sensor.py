# servicio_sensores/esquemas/esquema_sensor.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DatosSensor(BaseModel):
    id: Optional[str]        # En creación vendrá vacío, en respuesta tendrá valor
    sensor_id: str
    humedad: float
    temperatura: float
    radiacion: float
    lluvia: float
    fecha: datetime

    class Config:
        orm_mode = True
