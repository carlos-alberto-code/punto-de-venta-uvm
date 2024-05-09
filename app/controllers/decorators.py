from functools           import wraps
from sqlalchemy.exc      import IntegrityError


def validate_id(func):
    @wraps(func)
    def wrapper(repo, id: int, name: str, *args, **kwargs):
        if not repo.db.query(repo.model).get(id):
            raise ValueError(f'The id {id} does not exist.')
        return func(repo, id, name, *args, **kwargs)
    return wrapper


def validate_unique_name(func):
    @wraps(func)
    def wrapper(repo, id: int, name: str, *args, **kwargs):
        if repo.db.query(repo.model).filter(repo.model.name == name).first():
            raise ValueError(f'The name {name} already exists.')
        try:
            return func(repo, id, name, *args, **kwargs)
        except IntegrityError:
            repo.db.rollback()
            raise ValueError(f'The name {name} already exists.')
    return wrapper


def validate_name(func):
    def wrapper(repo, id: int, name: str, *args, **kwargs):
        if not name:
            raise ValueError('The name cannot be empty.')
        if not name.isalpha():
            raise ValueError('The name must contain only alphabetic characters.')
        if len(name) < 3 or len(name) > 20:
            raise ValueError('The name must be between 3 and 20 characters long.')
        return func(repo, id, name, *args, **kwargs)
    return wrapper