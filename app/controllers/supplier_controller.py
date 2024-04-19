from database.connection import get_db
from models.models import Supplier
class SupplierController:
    #comprobar si la categoria existe
    def id_supplier_exist(self,supplier_id: int):
        with get_db() as db:
            supplier= db.query(Supplier).filter(Supplier.id == supplier_id).first()
            return supplier is not None
    
    # Un método para comprobar si una categoria existe, mediante su nombre
    def name_supplier_exist(self, supplier_name: str):
         with get_db() as db:
            supplier = db.query(Supplier).filter(Supplier.name == supplier_name).first()
            return supplier is not None
    
    def get_supplier(self, supplier_id: int):
        if self.id_supplier_exist(supplier_id):
            with get_db() as db:
                supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
                return supplier
    def new_supplier(self, supplier_name: str):
        if self.name_supplier_exist(supplier_name):
            print('supplier already exists')
        with get_db() as db:
            supplier = db.query(Supplier).filter(Supplier.name == supplier_name).first()
            if supplier is not None:
                return None
            new_supplier = Supplier(name=supplier_name)
            db.add(new_supplier)
            db.commit()
    
    def edit_supplier(self, supplier_id: int, new_supplier_name: str):
        if not self.id_supplier_exist(supplier_id):
            print('supplier not found')
        with get_db() as db:
            supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
            if supplier is None:
                raise Exception('supplier not found')
            supplier.name = new_supplier_name
            db.commit()
            
    def delete_supplier(self, supplier_id):
        if not self.id_supplier_exist(supplier_id):
            print('supplier not found')
        with get_db() as db:
            supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
            db.delete(supplier)
            db.commit()
    
    def get_all(self):
        with get_db() as db:
            suppliers = db.query(Supplier).all()
            return suppliers