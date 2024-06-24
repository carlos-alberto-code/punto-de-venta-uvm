from typing import Dict, Any
import json

class Session:
    
    def __init__(self, username: str):
        self.__username = username
    
    def get_json_data(self) -> Dict[str, Any]:
        with open('roles/session_data.json', 'r') as file:
            data = json.load(file)
            return data
    
    @property
    def user_data(self) -> Dict[str, Any]:
        return self.get_json_data()[self.__username]

    def set_data_session(self, data: Dict[str, Any]) -> None:
        # Guarda los datos de la sesión en un archivo json. La clave es el nombre del usuario.
        pass