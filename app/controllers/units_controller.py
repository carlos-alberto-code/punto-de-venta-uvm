from database.connection import get_db
from models.models import Unit
from .data_checker import DataChecker

class UnitsController:

    def __init__(self) -> None:
        self._checker = DataChecker()

    def get_all_units(self) -> list[Unit]:
        '''
        Initially checks if there is data in the units table. If there is no data, it raises an exception.
        If there is data, it retrieves all the units from the database and returns them in a list 
        sorted alphabetically by the unit name.
        '''
        if not self._checker.exist_data_in(Unit):
            raise Exception(f'There is no data in the table "{Unit.__tablename__}".')
        with get_db() as db:
            units = db.query(Unit).order_by(Unit.name).all()
            return units
    
    def new_unit(self, name: str) -> None:
        '''
        Checks if the unit name already exists in the units table. If it already exists, it raises an exception.
        If it doesn't exist, it creates a new unit with the provided name and adds it to the units table.
        '''
        if self._checker.name_exist(name, Unit):
            raise Exception(f'The unit "{name.lower()}" already exists in the table "{Unit.__tablename__}".')
        with get_db() as db:
            unit = Unit(name=name.lower())
            db.add(unit)
            db.commit()
    
    def delete_unit(self, name: str) -> None:
        '''
        Checks if the unit name exists in the units table. If it doesn't exist, it raises an exception.
        If it exists, it deletes the unit from the units table.
        '''
        if not self._checker.name_exist(name, Unit):
            raise Exception(f'The unit "{name.lower()}" does not exist in the table "{Unit.__tablename__}".')
        with get_db() as db:
            unit = db.query(Unit).filter_by(name=name.lower()).first()
            db.delete(unit)
            db.commit()
    
    def update_unit(self, old_name: str, new_name: str) -> None:
        '''
        Checks if the unit name exists in the units table. If it doesn't exist, it raises an exception.
        If it exists, it checks if the new name already exists in the units table. If it already exists, it raises an exception.
        If the new name doesn't exist, it updates the unit name in the units table.
        '''
        if not self._checker.name_exist(old_name, Unit):
            raise Exception(f'The unit "{old_name.lower()}" does not exist in the table "{Unit.__tablename__}".')
        if self._checker.name_exist(new_name, Unit):
            raise Exception(f'The unit "{new_name.lower()}" already exists in the table "{Unit.__tablename__}".')
        with get_db() as db:
            unit = db.query(Unit).filter_by(name=old_name.lower()).first()
            if unit is not None:
                unit.name = new_name.lower()
                db.commit()
