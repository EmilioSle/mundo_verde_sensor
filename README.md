# mundo_verde_sensor
modulo de sensores

Estructura
servicio_sensores/
├── main.py                          # Punto de entrada (inicia FastAPI)
├── controladores/                  # Controladores que reciben las solicitudes HTTP
│   └── controlador_sensores.py
├── repositorios/                   # Acceso a base de datos
│   └── repositorio_datos_sensores.py
├── modelos/                        # Modelos ORM para la base de datos
│   └── entidad_sensor.py
├── esquemas/                       # Modelos Pydantic (para validación)
│   └── esquema_sensor.py
├── servicios/                      # Lógica del negocio / procesamiento
│   ├── detector_anomalias.py
│   └── predictor_sequia.py
├── modelos_ml/                     # IA/ML: predicción con modelos entrenados
│   ├── predictor_sequia.py
│   ├── modelo_entrenado.pkl
│   └── preprocesamiento.py
└── config/                         # Configuración de base de datos, etc.
    └── database.py


