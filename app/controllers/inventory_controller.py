from database.connection import get_db
from models.models import Product, Unit, Category, Brand


class InventoryController:

    # Un método para comprobar si un rol existe, mediante su id
    def id_product_exist(self, product_id: int):
        with get_db() as db:
            product = db.query(Product).filter(Product.id == product_id).first()
            return product is not None
    
    # Un método para comprobar si un rol existe, mediante su nombre
    def name_product_exist(self, product_name: str):
        with get_db() as db:
            product = db.query(Product).filter(Product.name == product_name).first()
            return product is not None
    
    def get_product(self, product_id: int):
        if self.id_product_exist(product_id):
            with get_db() as db:
                product = db.query(Product).filter(Product.id == product_id).first()
                return product
        
    def new_product(self, product_name: str):
        if self.name_product_exist(product_name):
            print('product already exists')
        with get_db() as db:
            product = db.query(Product).filter(Product.name == product_name).first()
            if product is not None:
                return None
            new_product = Product(name=product_name)
            db.add(new_product)
            db.commit()
    
    def edit_product(self, product_id: int, new_product_name: str):
        if not self.id_product_exist(product_id):
            print('product not found')
        with get_db() as db:
            product = db.query(Product).filter(Product.id == product_id).first()
            if product is None:
                raise Exception('product not found')
            product.name = new_product_name
            db.commit()
            
    def delete_product(self, product_id):
        if not self.id_product_exist(product_id):
            print('product not found')
        with get_db() as db:
            product = db.query(Product).filter(Product.id == product_id).first()
            db.delete(product)
            db.commit()

    def get_all(self):
        with get_db() as db:
            products = db.query(Product).all()
            return products


class UnitController:

    # Definir el crud para la tabla units

    def get_all_units(self):
        with get_db() as db:
            units = db.query(Unit).all()
            return units
    
    def new_unit(self, unit_name: str):
        with get_db() as db:
            unit = db.query(Unit).filter(Unit.name == unit_name).first()
            if unit is not None:
                return None
            new_unit = Unit(name=unit_name)
            db.add(new_unit)
            db.commit()
    
