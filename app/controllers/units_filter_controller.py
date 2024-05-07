from models.models import Unit
from .filter_interface import IFilter
from database.connection import get_db
from .crud_repository import CrudRepository


class UnitsFilterController(IFilter):

    def __init__(self) -> None:
        super().__init__()
        with get_db() as db:
            self.controller = CrudRepository(model=Unit, session=db)
            
    def get_all_values(self):
        with get_db() as db:
            return self.controller.get_all()
    
    def get_property_name(self):
        return Unit.__name__.capitalize()

    def search(self, value: str):
        with get_db() as db:
            controller = CrudRepository(model=Unit, session=db)
            return controller.search(value)
    
    def create(self, value: str):
        with get_db() as db:
            controller = CrudRepository(model=Unit, session=db)
            return controller.create(value)
    
