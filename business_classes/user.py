from naveasey.naveasey import Module


class User:

    users = {}

    def __init__(self, username: str, password: str, modules: list[Module]):
        self.username = username
        self.password = password
        self.__role: str = ''
        self.__modules: list[Module] = modules
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
    
    def add_module(self, module: Module):
        self.__modules.append(module)
        User.users[self.username] = self

    def remove_module(self, module: Module):
        self.__modules.remove(module)  
        User.users[self.username] = self

    def delete_user(self):
        del User.users[self.username]  

    def __repr__(self) -> str:
        return f'User({self.username})'
    