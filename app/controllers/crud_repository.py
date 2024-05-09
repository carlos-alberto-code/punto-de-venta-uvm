from typing         import Type
from sqlalchemy.orm import Session
from .decorators    import (
    validate_id,
    validate_name,
    validate_unique_name,
)


class CrudRepository:
    
    def __init__(self, model, session: Session) -> None:
        self.model = model
        self.db = session    

    # CRUD Methods    

    def get_all(self):
        return self.db.query(self.model)\
        .order_by(self.model.name)\
        .all()

    @validate_unique_name
    @validate_name
    def create(self, name: str):
        instance = self.model(name=name.lower())
        self.db.add(instance)
        self.db.commit()
    
    @validate_id
    def get_by_id(self, id: int):
        return self.db.query(self.model).get(id)
    
    @validate_id
    def delete(self, id: int):
        instance = self.db.query(self.model).get(id)
        self.db.delete(instance)
        self.db.commit()
    
    @validate_unique_name
    @validate_name
    @validate_id
    def update(self, id: int, new_name: str):
        instance = self.db.query(self.model).get(id)
        if instance is not None:
            instance.name = new_name.lower()
            self.db.commit()
    
    def search(self, name: str):
        return self.db.query(self.model)\
            .filter(self.model.name.ilike(f'%{name}%'))\
            .order_by(self.model.name)\
            .all()
