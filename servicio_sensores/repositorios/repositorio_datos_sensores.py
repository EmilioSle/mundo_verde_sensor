# servicio_sensores/repositorios/repositorio_datos_sensores.py

from sqlalchemy.orm import Session
from models.entidad_sensor import EntidadSensor
from esquemas.esquema_sensor import DatosSensor
import uuid

def guardar_sensor(db: Session, datos: DatosSensor):
    # Creamos una nueva entidad pasando todos los campos excepto el id (lo genera la base)
    nuevo = EntidadSensor(
        id=str(uuid.uuid4()),
        sensor_id=datos.sensor_id,
        humedad=datos.humedad,
        temperatura=datos.temperatura,
        radiacion=datos.radiacion,
        lluvia=datos.lluvia,
        fecha=datos.fecha
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    # Convertimos la entidad ORM a un objeto DatosSensor (Pydantic) para devolverlo
    return DatosSensor(
        id=nuevo.id,
        sensor_id=nuevo.sensor_id,
        humedad=nuevo.humedad,
        temperatura=nuevo.temperatura,
        radiacion=nuevo.radiacion,
        lluvia=nuevo.lluvia,
        fecha=nuevo.fecha
    )

def listar_sensores(db: Session):
    resultados = db.query(EntidadSensor).all()
    # Convertimos cada EntidadSensor a un DatosSensor
    lista = []
    for e in resultados:
        lista.append(
            DatosSensor(
                id=e.id,
                sensor_id=e.sensor_id,
                humedad=e.humedad,
                temperatura=e.temperatura,
                radiacion=e.radiacion,
                lluvia=e.lluvia,
                fecha=e.fecha
            )
        )
    return lista
