from abc import ABC, abstractmethod


class SearcherControllerInterface(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    def search(self, value: str):
        raise NotImplementedError
    
    @abstractmethod
    def create(self, value: str):
        raise NotImplementedError
    
    # @abstractmethod
    # def delete(self, value: str):
    #     raise NotImplementedError
