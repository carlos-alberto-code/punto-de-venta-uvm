from contextlib import contextmanager
from dotenv import load_dotenv
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from database.models import Base


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')
# NOTE: Si no existen modelos bien configurados a la base de datos, devolverá un archivo en la raíz del proyecto llamado test.db


# Estableciendo el motor de la base de datos
engine = create_engine(DATABASE_URL)# echo=True)

# Creando todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)

# Creating a SessionLocal class which will be used as a factory to create new Session objects
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