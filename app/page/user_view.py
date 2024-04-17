from abc import abstractmethod


class ViewStrategy:

    @abstractmethod
    def build(self):
        print(f'Construcción de la vista {self.__class__.__name__}')
        pass


class OwnerView(ViewStrategy):

    def build(self):
        return super().build()


class AdminView(ViewStrategy):

    def build(self):
        return super().build()


class EmployeeView(ViewStrategy):

    def build(self):
        return super().build()

class UserView:

    def __init__(self, view_strategy: ViewStrategy) -> None:
        self.view_strategy =view_strategy
    
    def build_view(self):
        return self.view_strategy.build()



class User:
    
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password