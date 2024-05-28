from abc import ABC, abstractmethod


class ControllerInterface(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: int, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def search(self, search_term: str):
        raise NotImplementedError
    

class FieldInterface(ABC):

    @abstractmethod
    def reset(self):
        raise NotImplementedError