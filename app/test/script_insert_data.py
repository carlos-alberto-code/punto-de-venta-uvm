"""
Este script se encarga de insertar datos en las tablas de la base de datos.
Los datos son simplemente de prueba, no son los datos que por ahora son reales, aunque se asemejan.
"""
import sys
sys.path.append('..')

from models.models import Unit, Category, Brand
from database.connection import get_db

units_data = ['kg', 'litro', 'pieza', 'metro', 'caja', 'bolsa']
categories_data = ['frutas', 'verduras', 'lácteos', 'carnes', 'bebidas', 'pan', 'dulces', 'abarrotes', 'limpieza', 'higiene']
brands_data = ['Coca-Cola', 'Bimbo', 'Lala', 'Alpura', 'Jumex', 'Zwan', 'Barcel', 'Gamesa', 'Sabritas', 'Pepsi', 'Knorr', 'Herdez', 'La Costeña', 'Nestlé', 'Danone', 'Kellogg\'s', 'Unilever', 'Colgate', 'P&G', 'Johnson & Johnson']

# Insertar datos en la tabla units
with get_db() as db:
    for unit in units_data:
        if not db.query(Unit).filter(Unit.name == unit).first():
            db.add(Unit(name=unit))
            db.commit()

# Insertar datos en la tabla categories
with get_db() as db:
    for category in categories_data:
        if not db.query(Category).filter(Category.name == category).first():
            db.add(Category(name=category))
            db.commit()

# Insertar datos en la tabla brands
with get_db() as db:
    for brand in brands_data:
        if not db.query(Brand).filter(Brand.name == brand).first():
            db.add(Brand(name=brand))
            db.commit()

print('Datos insertados correctamente.')