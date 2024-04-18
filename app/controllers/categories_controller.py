from database.connection import get_db
from models.models import Category
class CategorieController:
    #comprobar si la categoria existe
    def id_categorie_exist(self,categorie_id: int):
        with get_db() as db:
            categorie= db.query(Category).filter(Category.id == categorie_id).first()
            return categorie is not None
    
    # Un método para comprobar si una categoria existe, mediante su nombre
    def name_categorie_exist(self, categorie_name: str):
         with get_db() as db:
            categorie = db.query(Category).filter(Category.name == categorie_name).first()
            return categorie is not None
    
    def get_categorie(self, categorie_id: int):
        if self.id_categorie_exist(categorie_id):
            with get_db() as db:
                categorie = db.query(Category).filter(Category.id == categorie_id).first()
                return categorie
    def new_categorie(self, categorie_name: str):
        if self.name_categorie_exist(categorie_name):
            print('categorie already exists')
        with get_db() as db:
            categorie = db.query(Category).filter(Category.name == categorie_name).first()
            if categorie is not None:
                return None
            new_categorie = Category(name=categorie_name)
            db.add(new_categorie)
            db.commit()
    
    def edit_categorie(self, categorie_id: int, new_categorie_name: str):
        if not self.id_categorie_exist(categorie_id):
            print('categorie not found')
        with get_db() as db:
            categorie = db.query(Category).filter(Category.id == categorie_id).first()
            if categorie is None:
                raise Exception('categorie not found')
            categorie.name = new_categorie_name
            db.commit()
            
    def delete_categorie(self, categorie_id):
        if not self.id_categorie_exist(categorie_id):
            print('categorie not found')
        with get_db() as db:
            categorie = db.query(Category).filter(Category.id == categorie_id).first()
            db.delete(categorie)
            db.commit()
