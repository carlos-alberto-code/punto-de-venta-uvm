from typing import Any
from models.models import Base
from sqlalchemy.orm import Session
from database.connection import get_db
from sqlalchemy.exc import IntegrityError


def validate_name(func):
    def wrapper(self, name: str, *args, **kwargs):
        if not name:
            raise ValueError('The name cannot be empty.')
        if not all(char.isalnum() or char.isspace() for char in name):
            raise ValueError('The name must contain only alphanumeric characters and spaces.')
        if len(name) < 3 or len(name) > 20:
            raise ValueError('The name must be between 3 and 20 characters long.')
        return func(self, name, *args, **kwargs)
    return wrapper


# Decorador para comprobar si el id existe en la base de datos. Puede tomar cualquier modelo como argumento y una session
def validate_id_existence(model: Any, db: Session):
    def decorator(func):
        def wrapper(self, id: int, *args, **kwargs):
            if not db.query(model).get(id):
                raise ValueError(f'The id {id} does not exist.')
            return func(self, id, *args, **kwargs)
        return wrapper
    return decorator


def validate_unique(model: Any, field: str, db: Session):
    def decorator(func):
        def wrapper(self, value, *args, **kwargs):
            if db.query(model).filter(getattr(model, field) == value).first():
                raise ValueError(f'The {field} {value} already exists.')
            try:
                return func(self, value, *args, **kwargs)
            except IntegrityError:
                db.rollback()
                raise ValueError(f'The {field} {value} already exists.')
        return wrapper
    return decorator