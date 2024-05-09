from functools           import wraps
from sqlalchemy.exc      import IntegrityError


# Decorador para comprobar si el nombre cumple con las siguientes condiciones:
def validate_name(func):
    '''
    Decorador para comprobar si el nombre cumple con las siguientes condiciones:
    - No puede estar vacío.
    - Solo puede contener caracteres alfanuméricos y espacios.
    - Debe tener entre 3 y 20 caracteres de longitud.
    '''
    def wrapper(self, name: str, *args, **kwargs):
        if not name:
            raise ValueError('The name cannot be empty.')
        if not all(char.isalnum() or char.isspace() for char in name):
            raise ValueError('The name must contain only alphanumeric characters and spaces.')
        if len(name) < 3 or len(name) > 20:
            raise ValueError('The name must be between 3 and 20 characters long.')
        return func(self, name, *args, **kwargs)
    return wrapper


# Decorador para comprobar si un nombre que no debe repetirse ya existe en la base de datos.
def validate_unique_name(func):
    @wraps(func)
    def wrapper(repo, name: str, *args, **kwargs):
        print('Validating unique name...')
        if repo.db.query(repo.model).filter(repo.model.name == name).first():
            raise ValueError(f'The name {name} already exists.')
        try:
            return func(repo, name, *args, **kwargs)
        except IntegrityError:
            repo.db.rollback()
            raise ValueError(f'The name {name} already exists.')
    return wrapper


# Decorador para comprobar si el id existe en la base de datos.
def validate_id(func):
    @wraps(func)
    def wrapper(repo, id: int, *args, **kwargs):
        print('Validating id...')
        if not repo.db.query(repo.model).get(id):
            raise ValueError(f'The id {id} does not exist.')
        return func(repo, id, *args, **kwargs)
    return wrapper