import flet as ft

from users.session import Session
from naveasey.naveasey import Module
from modules.modules import Module as Rail



class User:

    users = {}

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.__session: Session = Session(username=username, password=password)
        self.__role: str = self.__session.data['role'] # type: ignore
        self.__module_names: list[str] = self.__session.data['modules'] # type: ignore
        self.__modules: list[Module] = [
            module for module_name, module 
            in Rail.repo.items() 
            if module_name in self.__module_names
        ]
        self.__theme_mode: str = self.__session.data['theme_mode'] # type: ignore
        User.users[username] = self
    
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
    