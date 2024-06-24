from users.user      import User
from users.session              import Session


class Autenticator:

    def __init__(self, username: str, password: str):
        self.__username         = username
        self.__password         = password

    def authenticate(self):
        pass

    def __is_authenticated(self):
        pass
