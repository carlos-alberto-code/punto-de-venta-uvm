from database.connection import get_db
from models.models import Brand, Category, Unit
from controllers.repository import Repository
from .filter_interface import IFilter


class BrandFilter(IFilter):

    def __init__(self) -> None:
        super().__init__()
        with get_db() as db:
            self.repository = Repository(Brand, db)

    def get_all(self):
        return self.repository.get_all()
    
    def search(self, value: str):
        return self.repository.search(value)
    
    def create(self, value: str) -> None:
        self.repository.create(name=value)