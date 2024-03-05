from models.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'mysql+mysqlconnector://carlosDB:93KnvK@localhost:3306/punto_de_venta_uvm'

# Estableciendo el motor de la base de datos
engine = create_engine(DATABASE_URI, echo=True)

# Creando todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)

# Creating a SessionLocal class which will be used as a factory to create new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency that can be used to get a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


