from abc import ABC, abstractmethod


class ControllerInterface(ABC):

    @abstractmethod
    def get_all(self):
        '''Return all the records in the database'''
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id: int):
        '''Return a record by its id'''
        raise NotImplementedError
    
    @abstractmethod
    def insert(self, **data):
        '''Insert a new record'''
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: int, **data):
        '''Update a record by its id'''
        raise NotImplementedError
    
    @abstractmethod
    def search(self, search_term: str):
        '''Search into the model for a record that matches the search term'''
        raise NotImplementedError