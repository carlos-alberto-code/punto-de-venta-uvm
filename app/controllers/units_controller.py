from .database_exceptions import EmptyTableException, ValueNotFoundException, ValueAlreadyExistsException
from .checker import Checker, validate_name
from database.connection import get_db
from sqlalchemy.orm import Session
from models.models import Unit


class UnitRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_units(self):
        return self.db.query(Unit).order_by(Unit.name).all()

    def create_unit(self, name: str):
        unit = Unit(name=name.lower())
        self.db.add(unit)
        self.db.commit()

    def delete_unit(self, name: str):
        unit = self.db.query(Unit).filter_by(name=name.lower()).first()
        self.db.delete(unit)
        self.db.commit()

    def update_unit(self, old_name: str, new_name: str):
        unit = self.db.query(Unit).filter_by(name=old_name.lower()).first()
        if unit is not None:
            unit.name = new_name.lower()
            self.db.commit()

    def search_unit(self, name: str):
        return self.db.query(Unit).filter(Unit.name.ilike(f'%{name}%')).all()


class UnitsController:

    def __init__(self) -> None:
        self._table_name = Unit.__tablename__
        self._checker = Checker()
    
    @property
    def table_name(self) -> str:
        return self._table_name

    def get_all_units(self) -> list[Unit]:
        with get_db() as db:
            if not self._checker.exist_data_in(Unit, db):
                raise EmptyTableException(Unit.__tablename__)
            repo = UnitRepository(db)
            units = repo.get_all_units()
            return units
    
    @validate_name
    def create_unit(self, name: str) -> None:
        with get_db() as db:
            if self._checker.name_exist(name, Unit, db):
                raise ValueAlreadyExistsException(name, Unit.__tablename__)
            repo = UnitRepository(db)
            repo.create_unit(name)
    
    @validate_name
    def delete_unit(self, name: str) -> None:
        with get_db() as db:
            if not self._checker.name_exist(name, Unit, db):
                raise ValueNotFoundException(name, Unit.__tablename__)
            repo = UnitRepository(db)
            repo.delete_unit(name)

    @validate_name
    def update_unit(self, old_name: str, new_name: str) -> None:
        with get_db() as db:
            if self._checker.name_exist(new_name, Unit, db):
                raise ValueAlreadyExistsException(new_name, Unit.__tablename__)
            repo = UnitRepository(db)
            repo.update_unit(old_name, new_name)

    def search_unit(self, name: str):
        with get_db() as db:
            repo = UnitRepository(db)
            units = repo.search_unit(name)
            return units
        