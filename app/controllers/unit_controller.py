from models.models import Unit
from database.connection import get_db


class UnitControllerTest:

    def new_unit(self, name: str):
        with get_db() as db:
            unit = db.query(Unit).filter(Unit.name == name).first()
            # si la unidad no existe, entonces se registra, de lo contrario se emite un mensaje
            if unit is not None:
                print('Unit already exists')
            else:
                unit = Unit(name=name)
                db.add(unit)
                db.commit()
        