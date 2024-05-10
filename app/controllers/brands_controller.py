from .database_exceptions import EmptyTableException, ValueAlreadyExistsException, ValueNotFoundException
from .checker import Checker, validate_name
from database.connection import get_db
from sqlalchemy.orm import Session
from models.models import Brand


class BrandRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_brands(self):
        return self.db.query(Brand).order_by(Brand.name).all()

    def create_brand(self, name: str):
        brand = Brand(name=name.lower())
        self.db.add(brand)
        self.db.commit()

    def delete_brand(self, name: str):
        brand = self.db.query(Brand).filter_by(name=name.lower()).first()
        self.db.delete(brand)
        self.db.commit()

    def update_brand(self, old_name: str, new_name: str):
        brand = self.db.query(Brand).filter_by(name=old_name.lower()).first()
        if brand is not None:
            brand.name = new_name.lower()
            self.db.commit()

    def search_brand(self, name: str):
        return self.db.query(Brand).filter(Brand.name.ilike(f'%{name}%')).all()


class BrandsController:
    def __init__(self) -> None:
        self._table_name = Brand.__tablename__
        self._checker = Checker()
    
    @property
    def table_name(self) -> str:
        return self._table_name

    def get_all_brands(self) -> list[Brand]:
        with get_db() as db:
            if not self._checker.exist_data_in(Brand, db):
                raise EmptyTableException(Brand.__tablename__)
            repo = BrandRepository(db)
            brands = repo.get_all_brands()
            return brands
    
    @validate_name
    def create_brand(self, name: str) -> None:
        with get_db() as db:
            if self._checker.name_exist(name, Brand, db):
                raise ValueAlreadyExistsException(name, Brand.__tablename__)
            repo = BrandRepository(db)
            repo.create_brand(name)
    
    @validate_name
    def delete_brand(self, name: str) -> None:
        with get_db() as db:
            if not self._checker.name_exist(name, Brand, db):
                raise ValueNotFoundException(name, Brand.__tablename__)
            repo = BrandRepository(db)
            repo.delete_brand(name)

    @validate_name
    def update_brand(self, old_name: str, new_name: str) -> None:
        with get_db() as db:
            if self._checker.name_exist(new_name, Brand, db):
                raise ValueAlreadyExistsException(new_name, Brand.__tablename__)
            repo = BrandRepository(db)
            repo.update_brand(old_name, new_name)

    def search_brand(self, name: str):
        with get_db() as db:
            repo = BrandRepository(db)
            brands = repo.search_brand(name)
            return brands