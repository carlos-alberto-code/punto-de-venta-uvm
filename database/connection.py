# Variables de entorno
from dotenv import load_dotenv
import os

load_dotenv()
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}"
engine = create_engine(DATABASE_URL)  # Cambia echo a False en producción

# Migraciones automáticas con Alembic (opcional)
# Este bloque puede ser opcional y solo para desarrollo. En producción, considera ejecutar las migraciones manualmente.
# from alembic.config import Config
# from alembic import command

# def run_migrations():
#     alembic_cfg = Config("alembic.ini")
#     command.upgrade(alembic_cfg, "head")

# if os.getenv('ENV') != 'production':
#     run_migrations()

# Modelos y gestión del contexto de la base de datos
from database.models import Base  # Asegúrate de que este import sea correcto
from contextlib import contextmanager

# No llamamos a create_all, ya que las migraciones de Alembic deben manejar esto
# Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    """
    Dependency that can be used to get a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
