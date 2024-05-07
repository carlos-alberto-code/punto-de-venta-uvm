from typing         import Type
from sqlalchemy.orm import Session
from .decorators    import validate_name


class CrudRepository:
    
    def __init__(self, model, session: Session) -> None:
        self.model = model
        self.db = session

    def get_all(self):
        return self.db.query(self.model).order_by(self.model.name).all()
    
    # TODO: Decorador: Observar si el campo es de valores únicos para comprobar si ese valor ya existe. Si no es de valores únicos, permitirá registrar.
    @validate_name
    def create(self, name: str):
        instance = self.model(name=name.lower())
        self.db.add(instance)
        self.db.commit()
    
    # TODO: Anotación para comprobar si el id existe
    def delete(self, id: int):
        instance = self.db.query(self.model).get(id)
        self.db.delete(instance)
        self.db.commit()
    
    # TODO: Anotación para comprobar si el id existe
    # TODO: Anotación para comprobar si el nuevo nombre ya existe
    @validate_name
    def update(self, id: int, new_name: str):
        instance = self.db.query(self.model).get(id)
        if instance is not None:
            instance.name = new_name.lower()
            self.db.commit()
    
    @validate_name
    def search(self, name: str):
        return self.db.query(self.model)\
            .filter(self.model.name.ilike(f'%{name}%'))\
            .order_by(self.model.name)\
            .all()
