from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def sync(self, subject: 'Subject'):
        pass

class Subject(ABC):
    
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


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
    
    # @abstractmethod
    # def delete(self, id: int):
    #     raise NotImplementedError


class FieldInterface(ABC):
    """
    This interface represents a field in a form.
    It provides methods to get the value of the field and reset it to its initial state.
    """

    @abstractmethod
    def value(self):
        """
        Return the value of the field.
        """
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        """
        Reset the field to its initial state.
        """
        raise NotImplementedError


# class FormInterface(ABC):
#     """
#     This interface represents a form.
#     It provides methods to initialize the form with fields, reset the form and save the form data into the database.
#     """

#     @abstractmethod
#     def __init__(self, *fields: FieldInterface):
#         """
#         Initialize the form with the fields provided.
#         """
#         self.fields = fields

#     @abstractmethod
#     def reset(self):
#         """
#         Reset the form to its initial state.
#         """
#         raise NotImplementedError

#     @abstractmethod
#     def save(self):
#         """
#         Save the form data into the database.
#         """
#         raise NotImplementedError
