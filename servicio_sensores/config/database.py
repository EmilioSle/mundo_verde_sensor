# servicio_sensores/config/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carga las variables de entorno definidas en .env
load_dotenv()

# Construye la URL de conexión a PostgreSQL
DB_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Crea el engine de SQLAlchemy
engine = create_engine(DB_URL)

# sessionmaker devuelve un constructor de sesiones (SessionLocal)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base es la clase que heredarán todas las entidades ORM
Base = declarative_base()
