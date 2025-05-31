import joblib
import numpy as np
import os

class PredictorSequia:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "modelo_entrenado.pkl")
        self.modelo = joblib.load(path)

    def predecir(self, datos: dict) -> float:
        entrada = np.array([[datos["humedad"], datos["temperatura"], datos["radiacion"], datos["lluvia"]]])
        return round(self.modelo.predict_proba(entrada)[0][1], 3)
