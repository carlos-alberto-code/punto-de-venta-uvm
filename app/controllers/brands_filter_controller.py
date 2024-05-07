from models.models import Brand
from .filter_interface import IFilter
from database.connection import get_db
from .crud_repository import CrudRepository


class BrandsFilterController(IFilter):

    def get_all_values(self):
        with get_db() as db:
            controller = CrudRepository(model=Brand, session=db)
            return controller.get_all()
    
    def get_property_name(self):
        return Brand.__name__.capitalize()

    def search(self, value: str):
        with get_db() as db:
            controller = CrudRepository(model=Brand, session=db)
            return controller.search(value)
    
    def create(self, value: str):
        with get_db() as db:
            controller = CrudRepository(model=Brand, session=db)
            return controller.create(value)
    
