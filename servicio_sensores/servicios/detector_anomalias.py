def detectar_anomalias(datos):
    if datos.humedad < 10 or datos.temperatura > 45:
        return True
    return False
