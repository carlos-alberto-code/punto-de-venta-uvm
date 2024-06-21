from business_classes.user      import User
from roles.session              import Session
from controllers.controllers    import UserController


class Autenticator:
    def __init__(self, username: str, password: str):
        self.__username         = username
        self.__password         = password
        self.__user_controller  = UserController()

    def authenticate(self):
        if self.__is_authenticated():
            # user_session_data = Session(self.__username).get_data_session()
            # return User(
            #     username=self.__username,
            #     password=self.__password,
            #     modules=[]
            # )
            print('Usuario autenticado')
        else:
            if not self.__user_controller.username_exists(self.__username):
                return f'El usuario "{self.__username}" no existe!'
            if not self.__user_controller.password_exists(self.__password):
                return 'Contraseña incorrecta'

    def __is_authenticated(self):
        if self.__user_controller.username_exists(self.__username)\
            and self.__user_controller.password_exists(self.__password):
            return True
