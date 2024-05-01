import sys
sys.path.append('..')

from models.models import Supplier
from app.database.connection import get_db

suppliers_data = ['The Coca-Cola Company', 'Grupo Bimbo', 'Zwan Food Group', 'Grupo Jumex', 'PepsiCo', 'Unilever', 'Grupo Herdez', 'Nestlé', 'La Costeña', 'Colgate-Palmolive', 'Procter & Gamble (P&G)', 'Johnson & Johnson']

#Insertar datos en la tabla proveedores
with get_db() as db:
    for supplier in suppliers_data:
        if not db.query(Supplier).filter(Supplier.name == supplier).first():
            db.add(Supplier(name=supplier))
            db.commit()

print('Datos insertados correctamente')