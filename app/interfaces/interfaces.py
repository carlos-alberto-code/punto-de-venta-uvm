from abc import ABC, abstractmethod


class ControllerInterface(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
    
    @abstractmethod

    def get_by_id(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def create(self, **data):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: int, **data):
        raise NotImplementedError
    
    @abstractmethod
    def search(self, search_term: str):
        raise NotImplementedError
    
    # @abstractmethod
    # def delete(self, id: int):
    #     raise NotImplementedError


class FieldInterface(ABC):

    @abstractmethod
    def reset(self):
        raise NotImplementedError