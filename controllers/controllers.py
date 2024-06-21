from decimal import Decimal
from typing import Dict, List, Union
from sqlalchemy import or_

from database.connection import get_db
from database.models import (
    Product, Unit, Category, Brand, Supplier, Purchase, User, Role
)

from controllers.repository import Repository, PurchaseRepository
from controllers.ControllerInterface import ControllerInterface


class ProductController(ControllerInterface):

    def __init__(self) -> None:
        with get_db() as db:
            self.repo = Repository(model=Product, session=db)
    
    def get_all(self):
        with get_db() as db:
            return db.query(
                Product.sku,
                Product.quantity,
                Product.cost_price,
                Product.selling_price,
                Product.reorder_level,
                Unit.name.label('unit'),
                Category.name.label('category'),
                Brand.name.label('brand')
            ).join(Unit, Product.unit_id == Unit.id)\
            .join(Category, Product.category_id == Category.id)\
            .join(Brand, Product.brand_id == Brand.id)\
            .all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)
    
    def insert(self, **data):
        return self.repo.create(**data)
    
    def update(self, id: int, **data):
        return self.repo.update(id, **data)
    
    def search(self, search_term: str):
        with get_db() as db:
            return db.query(
                Product.sku,
                Product.quantity,
                Product.cost_price,
                Product.selling_price,
                Product.reorder_level,
                Unit.name.label('unit'),
                Category.name.label('category'),
                Brand.name.label('brand')
            ).join(Unit, Product.unit_id == Unit.id)\
            .join(Category, Product.category_id == Category.id)\
            .join(Brand, Product.brand_id == Brand.id)\
            .filter(or_(
                Unit.name.ilike(f'%{search_term}%'),
                Category.name.ilike(f'%{search_term}%'),
                Brand.name.ilike(f'%{search_term}%')
            ))\
            .limit(10)\
            .all()


class UnitController(ControllerInterface):

    def __init__(self) -> None:
        with get_db() as db:
            self.repo = Repository(model=Unit, session=db)
    
    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)
    
    def insert(self, **data):
        return self.repo.create(**data)
    
    def update(self, id, **data):
        self.repo.update(id, **data)
    
    def search(self, search_term: str):
        with get_db() as db:
            return db.query(Unit).filter(Unit.name.ilike(f'%{search_term}%')).limit(10).all()


class CategoryController(ControllerInterface):

    def __init__(self) -> None:
        with get_db() as db:
            self.repo = Repository(model=Category, session=db)
    
    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)
    
    def insert(self, **data):
        return self.repo.create(**data)
    
    def update(self, id, **data):
        self.repo.update(id, **data)
    
    def search(self, search_term: str):
        with get_db() as db:
            return db.query(Category).filter(Category.name.ilike(f'%{search_term}%')).limit(10).all()


class BrandController(ControllerInterface):

    def __init__(self) -> None:
        with get_db() as db:
            self.repo = Repository(model=Brand, session=db)
    
    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)
    
    def insert(self, **data):
        return self.repo.create(**data)
    
    def update(self, id, **data):
        self.repo.update(id, **data)
    
    def search(self, search_term: str):
        with get_db() as db:
            return db.query(Brand).filter(Brand.name.ilike(f'%{search_term}%')).limit(10).all()


class SuplierController(ControllerInterface):

    def __init__(self) -> None:
        with get_db() as db:
            self.repo = Repository(model=Supplier, session=db)
    
    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)
    
    def insert(self, **data):
        return self.repo.create(**data)
    
    def update(self, id, **data):
        self.repo.update(id, **data)
    
    def search(self, search_term: str):
        with get_db() as db:
            return db.query(Supplier).filter(Supplier.name.ilike(f'%{search_term}%')).limit(10).all()


class PurchaseDetailController:

    def __init__(self) -> None:
        with get_db() as db:
            self.repo = PurchaseRepository(model=Purchase, session=db)
    
    def create_with_details(self, details: List[Dict[str, Union[int, Decimal]]], **kwargs):
        return self.repo.create_with_details(details, **kwargs)


class UserController(ControllerInterface):

    def __init__(self) -> None:
        with get_db() as db:
            self.repo = Repository(model=User, session=db)
    
    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)
    
    def insert(self, **data):
        return self.repo.create(**data)
    
    def update(self, id, **data):
        self.repo.update(id, **data)
    
    def search(self, search_term: str):
        with get_db() as db:
            return db.query(Product).filter(Product.sku.ilike(f'%{search_term}%')).limit(10).all()
    
    def username_exists(self, username: str):
            """
            Comprueba si existe el username especificado.

            Args:
                username (str): El nombre de usuario a comprobar.

            Returns:
                bool: True si existe un usuario con el nombre de usuario especificado, False de lo contrario.
            """
            with get_db() as db:
                return db.query(User).filter(User.username == username).first() is not None
    
    def password_exists(self, password: str):
            """
            Comprueba si existe la contraseña especificada.

            Args:
                password (str): La contraseña a comprobar.

            Returns:
                bool: True si existe un usuario con la contraseña especificada, False de lo contrario.
            """
            with get_db() as db:
                return db.query(User).filter(User.password == password).first() is not None
