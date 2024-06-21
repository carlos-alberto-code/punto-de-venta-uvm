from typing import Dict, Any

class Session:
    
    def __init__(self, username: str):
        self.__username = username
    
    def get_data_session(self) -> Dict[str, Any]:
        # Devuelve los datos del archivo json correspondiente al usuario. Sólo devuelve el valor que es un diccionario con los datos de sesión; pues la clave es el nombre del usuario.
        return {
            'username': self.__username,
            'modules': []
        }

    def set_data_session(self, data: Dict[str, Any]) -> None:
        # Guarda los datos de la sesión en un archivo json. La clave es el nombre del usuario.
        pass