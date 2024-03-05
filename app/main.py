from sqlalchemy import text
from database.connection import engine, get_db
from models.models import Base, Marca, Categoria, Units

from contextlib import contextmanager


# Verificar la conexión a la base de datos
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Conexión a la base de datos establecida:", result.fetchall())
except Exception as e:
    print("Error al conectar con la base de datos:", e)

@contextmanager
def get_db_context():
    db = next(get_db())
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Probar la creación de un nuevo producto y su inserción en la base de datos
try:
    with get_db_context() as db:
        nuevo_producto = Marca(
            nombre='Quaker'
        )
        db.add(nuevo_producto)
        db.commit()
        print("Producto agregado exitosamente.")
except Exception as e:
    print("Error al agregar el producto:", e)
