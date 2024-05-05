import random, sys
sys.path.append('..')

from app.database.connection import get_db
from models.models import Supplier

#Comprobar si la tabla Suppliers tiene registros
def exist_data():
    with get_db() as db:
        suppliers = db.query(Supplier).all()
        if not suppliers:
            return False
        return True

#Una funcion para obtener todos los proveedores
def get_suppliers():
    with get_db() as db:
        suppliers = db.query(Supplier).all()
        return suppliers

if exist_data():
    with get_db() as db:
        if not db.query(Supplier).first():
            for i in range(20):
                proveedor = Supplier(
                    id = i+1,
                    
                )