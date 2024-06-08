"""
Este script se encarga de insertar datos en las tablas de relación de la tabla productos de la base de datos.
Los datos son simplemente de prueba, no son los datos que por ahora son reales, aunque se asemejan a lo que se espera en el futuro.
"""

from database.models import Unit, Category, Brand
from database.connection import get_db

units_data = ['KILOGRAMO', 'LITRO', 'PIEZA', 'METRO', 'CAJA', 'BOLSA']
categories_data = ['FRUTAS', 'VERDURAS', 'LÁCTEOS', 'CARNES', 'BEBIDAS', 'PAN', 'DULCES', 'ABARROTES', 'LIMPIEZA', 'HIGIENE']
brands_data = ['COCA-COLA', 'BIMBO', 'LALA', 'ALPURA', 'JUMEX', 'ZWAN', 'BARCEL', 'GAMESA', 'SABRITAS', 'PEPSI', 'KNORR', 'HERDEZ', 'LA COSTEÑA', 'NESTLÉ', 'DANONE', 'KELLOGG\'S', 'UNILEVER', 'COLGATE', 'P&G', 'JOHNSON & JOHNSON']

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
