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
            raise Exception(f'There are no data in the table "{Unit.__tablename__}".')
        with get_db() as db:
            units = db.query(Unit).order_by(Unit.name).all()
            return units