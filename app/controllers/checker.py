from typing import Any
from sqlalchemy.orm import Session
from database.connection import get_db
from models.models import Base


class Checker:

    def exist_data_in(self, model: Any, db: Session) -> bool:
        return db.query(model).first() is not None
    
    def name_exist(self, name: str, model: Any, db: Session) -> bool:
        return db.query(model).filter_by(name=name).first() is not None


def validate_name(func):
    def wrapper(self, name: str, *args, **kwargs):
        if not isinstance(name, str):
            raise TypeError(f'The name must be a string, not {type(name).__name__}.')
        if not name:
            raise ValueError('The name cannot be empty.')
        if not name.isalnum():
            raise ValueError('The name must contain only alphanumeric characters.')
        if len(name) < 3 or len(name) > 20:
            raise ValueError('The name must be between 3 and 20 characters long.')
        return func(self, name, *args, **kwargs)
    return wrapper