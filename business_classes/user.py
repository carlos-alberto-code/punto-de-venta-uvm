import flet as ft
from roles.session import Session
from naveasey.naveasey import Module


class User:

    users = {}

    def __init__(self, username: str, password: str):
        self.username                = username
        self.password                = password
        self.__session: Session      = Session(username=username)
        self.__role: str             = self.__session.user_data['role']
        self.__modules: list[Module] = self.__session.user_data['modules']
        self.__theme_mode: str       = self.__session.user_data['theme_mode']
        User.users[username]         = self
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, role: str):
        self.__role = role
    
    @property
    def modules(self):
        return self.__modules
    
    @property
    def theme_mode(self):
        return self.__theme_mode
    
    def add_module(self, module: Module):
        self.__modules.append(module)
        User.users[self.username] = self
        # TODO: Actualizar el JSON

    def remove_module(self, module: Module):
        self.__modules.remove(module)  
        User.users[self.username] = self
        # TODO: Actualizar el JSON

    def delete_user(self):
        del User.users[self.username]  

    def __repr__(self) -> str:
        return f'User(username={self.username}, role={self.__role},  theme_mode={self.__theme_mode}, modules={self.__modules})'
    