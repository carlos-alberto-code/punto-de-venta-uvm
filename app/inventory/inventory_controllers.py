from database.connection import get_db
from controllers.repository import Repository
from database.models import Product, Unit, Brand, Category

from naveasy.interfaces import ControllerInterface as Controller


class ProductController(Controller):

    def __init__(self) -> None:
        super().__init__()
        with get_db() as db:
            self.repo = Repository(Product, db)

    def get_all(self):
        return self.repo.get_all()

    def create(self, **kwargs):
        self.repo.create(**kwargs)

    def update(self, id: int, **kwargs):
        pass

    def search(self, search_term: str):
        pass


class UnitController(Controller):

    def __init__(self) -> None:
        super().__init__()
        with get_db() as db:
            self.repo = Repository(Unit, db)

    def get_all(self):
        return self.repo.get_all()

    def create(self, **kwargs):
        self.repo.create(**kwargs)

    def update(self, id: int, **kwargs):
        pass

    def search(self, search_term: str):
        pass


class BrandController(Controller):
    
        def __init__(self) -> None:
            super().__init__()
            with get_db() as db:
                self.repo = Repository(Brand, db)
    
        def get_all(self):
            return self.repo.get_all()
    
        def create(self, **kwargs):
            self.repo.create(**kwargs)
    
        def update(self, id: int, **kwargs):
            pass
    
        def search(self, search_term: str):
            pass


class CategoryController(Controller):

    def __init__(self) -> None:
        super().__init__()
        with get_db() as db:
            self.repo = Repository(Category, db)

    def get_all(self):
        return self.repo.get_all()

    def create(self, **kwargs):
        self.repo.create(**kwargs)

    def update(self, id: int, **kwargs):
        pass

    def search(self, search_term: str):
        pass

