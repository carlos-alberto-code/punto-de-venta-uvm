# Crearemos los decoradores que nos ayudarán a validar los datos que se envían a la base de datos.
# Otro tipo de decoradores que podríamos crear serían los que se encarguen de manejar las excepciones que se generen en la base de datos.
# Y un último tipo de decoradores serían los que se encarguen de manejar la autenticación de los usuarios.


def validate_name(func):
    """
    A decorator function that validates the name parameter.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    Raises:
        TypeError: If the name parameter is not a string.
        ValueError: If the name parameter is empty, contains non-alphabetic characters, or exceeds 50 characters in length.
    """
    def wrapper(name: str, *args, **kwargs):
        if not isinstance(name, str):
            raise TypeError(f'The name must be a string, not {type(name).__name__}.')
        if not name:
            raise ValueError('The name cannot be empty.')
        if not name.isalpha():
            raise ValueError('The name must contain only letters.')
        if len(name) > 50:
            raise ValueError('The name must be less than 50 characters long.')
        return func(name, *args, **kwargs)
    
    return wrapper


