class UserViews:

    def __init__(self) -> None:
        self._modules = {}
    
    def __getitem__(self, key):
        return self._modules[key]
    
    def __len__(self):
        return len(self._modules)
    
    def __iter__(self):
        return iter(self._modules)

    def modules(self):
        pass



class Admin(UserViews):

    def modules(self):
        return super().modules()


class Employee(UserViews):

    def modules(self):
        return super().modules()