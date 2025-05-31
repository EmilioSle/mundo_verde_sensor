# servicio_sensores/modelos/entidad_sensor.py

from sqlalchemy import Column, String, Float, DateTime
from config.database import Base

class EntidadSensor(Base):
    __tablename__ = "datos_sensores"

    id = Column(String, primary_key=True, index=True)
    sensor_id = Column(String, nullable=False)
    humedad = Column(Float, nullable=False)
    temperatura = Column(Float, nullable=False)
    radiacion = Column(Float, nullable=False)
    lluvia = Column(Float, nullable=False)
    fecha = Column(DateTime, nullable=False)
