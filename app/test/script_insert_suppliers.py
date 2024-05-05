import sys, random
sys.path.append('..')

from models.models import Supplier
from database.connection import get_db

suppliers_data = ['The Coca-Cola Company', 'Grupo Bimbo', 'Zwan Food Group', 'Grupo Jumex', 'PepsiCo', 'Unilever', 'Grupo Herdez', 'Nestlé', 'La Costeña', 'Colgate-Palmolive', 'Procter & Gamble (P&G)', 'Johnson & Johnson']

#Insertar datos en la tabla proveedores
with get_db() as db:
    if not db.query(Supplier).first():
        for i in range(len(suppliers_data)):
            supplier = Supplier(
                id=i+1,
                name=suppliers_data[i],
                phone=random.randint(1000000000,9999999999)
            )
            db.add(supplier)
        db.commit()
        print('Datos insertados correctamente')
    else:
        print('Ya existen proveedores en la base de datos')