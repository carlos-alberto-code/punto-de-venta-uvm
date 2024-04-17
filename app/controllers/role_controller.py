from database.connection import get_db
from models.models import Role


class RoleController:

    # Un método para comprobar si un rol existe, mediante su id
    def id_role_exist(self, role_id: int):
        with get_db() as db:
            role = db.query(Role).filter(Role.id == role_id).first()
            return role is not None
    
    # Un método para comprobar si un rol existe, mediante su nombre
    def name_role_exist(self, role_name: str):
        with get_db() as db:
            role = db.query(Role).filter(Role.name == role_name).first()
            return role is not None
    
    def get_role(self, role_id: int):
        if self.id_role_exist(role_id):
            with get_db() as db:
                role = db.query(Role).filter(Role.id == role_id).first()
                return role
        
    def new_role(self, role_name: str):
        if self.name_role_exist(role_name):
            print('Role already exists')
        with get_db() as db:
            role = db.query(Role).filter(Role.name == role_name).first()
            if role is not None:
                return None
            new_role = Role(name=role_name)
            db.add(new_role)
            db.commit()
    
    def edit_role(self, role_id: int, new_role_name: str):
        if not self.id_role_exist(role_id):
            print('Role not found')
        with get_db() as db:
            role = db.query(Role).filter(Role.id == role_id).first()
            if role is None:
                raise Exception('Role not found')
            role.name = new_role_name
            db.commit()
            
    def delete_role(self, role_id):
        if not self.id_role_exist(role_id):
            print('Role not found')
        with get_db() as db:
            role = db.query(Role).filter(Role.id == role_id).first()
            db.delete(role)
            db.commit()

    def get_all(self):
        with get_db() as db:
            roles = db.query(Role).all()
            return roles
