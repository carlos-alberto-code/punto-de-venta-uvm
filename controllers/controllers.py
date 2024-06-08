from sqlalchemy import or_

from database.connection import get_db
from database.models import Product, Unit, Category, Brand

from controllers.repository import Repository
from interfaces.ControllerInterface import ControllerInterface


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
        