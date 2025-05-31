from modelos_ml.predictor_sequia import PredictorSequia

predictor = PredictorSequia()

def predecir_sequia(datos):
    return predictor.predecir(datos.dict())
