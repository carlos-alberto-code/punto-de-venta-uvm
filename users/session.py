import json
from typing import Dict, Any

def get_json_data() -> Dict[str, Any]:
    with open('users/session_data.json', 'r') as json_file:
        data = json.load(json_file)
        return data


class Session:
    
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self._json_data  = get_json_data()
    
    @property
    def data(self) -> Dict[str, Any] | str:
        if not self.user_exists():
            return f'El usuario {self.__username} no existe.'
        if not self.password_is_correct():
            return 'La contraseña es incorrecta.'
        else:
            return get_json_data()[self.__username]

    def user_exists(self) -> bool:
        return self.__username in self._json_data
    
    def password_is_correct(self) -> bool:
        return self.__password == self._json_data[self.__username]['password']
