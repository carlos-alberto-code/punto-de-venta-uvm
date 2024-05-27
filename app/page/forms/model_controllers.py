from database.connection import get_db
from controllers.repository import Repository
from page.interfaces.ControllerInterface import IController
from database.models import Unit, Category, Brand, Product


class UnitController(IController):

    def __init__(self):
        with get_db() as db:
            self.repository = Repository(Unit, db)
    
    def get_all(self):
        return self.repository.get_all()
    
    def search(self, value: str):
        return self.repository.search(value)
    
    def create(self, value: str):
        return self.repository.create(value)