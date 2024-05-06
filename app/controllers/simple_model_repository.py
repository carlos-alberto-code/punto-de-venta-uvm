from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from .decorators import validate_name


class SimpleModelRepository:
    
    def __init__(self, model: Type[declarative_base], session: Session) -> None: # type: ignore
        self.model = model
        self.db = session

    def get_all(self):
        return self.db.query(self.model).order_by(self.model.name).all()
    
    @validate_name
    def create(self, name: str):
        instance = self.model(name=name.lower())
        self.db.add(instance)
        self.db.commit()
    
    @validate_name
    def delete(self, name: str):
        instance = self.db.query(self.model).filter_by(name=name.lower()).first()
        self.db.delete(instance)
        self.db.commit()
    
    @validate_name
    def update(self, old_name: str, new_name: str):
        instance = self.db.query(self.model).filter_by(name=old_name.lower()).first()
        if instance is not None:
            instance.name = new_name.lower()
            self.db.commit()
    
    @validate_name
    def search(self, name: str):
        return self.db.query(self.model).filter(self.model.name.ilike(f'%{name}%')).all()
