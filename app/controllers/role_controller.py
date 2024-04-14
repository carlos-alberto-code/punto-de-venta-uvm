from database.connection import get_db
from models.models import Role


class RoleController:

    def __init__(self) -> None:
        self.db = next(get_db())
    
    def new_role(self, role_name: str):

        new_role = Role(name=role_name)
        self.db.add(new_role)
        self.db.commit()
    
    def edit_role(self, role_id: int):
        pass

    def delete_role(self, role_id):
        pass

    def get_role(self, role_id: int):
        pass

    def get_all(self):
        pass


class RoleTest:

    def __init__(self) -> None:
        self._roles = {
            1: 'propietario',
            2: 'administrador',
            3: 'empleado'
        }
    
    def new_role(self, role_name: str):
        self._roles[len(self._roles)] = role_name
    
    def get_role(self, role_id: int):
        return self._roles[role_id]
    
    def delete_role(self, role_id: int):
        del self._roles[role_id]
    
    def edit_role_name(self, role_id: int, new_role_name: str):
        self._roles[role_id] = new_role_name
    
    def get_all(self):
        return self._roles