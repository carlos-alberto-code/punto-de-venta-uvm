from abc import ABC, abstractmethod


class IFilter(ABC):
    # Esta será una interfaz que debrán usar controladores simples para implementar la funcionalidad de búsqueda y filtrado.
    # Esta interfaz es define un contrato de sólo lectura y creación, es decir CR del CRUD.

    @abstractmethod
    def get_property_name(self):
        # Para obtener el nombre de la propiedad que se está filtrando.
        raise NotImplementedError
    
    @abstractmethod
    def get_all_values(self):
        # Para obtener todos los valores y mostrarlos en el SearchBarFilter.
        raise NotImplementedError

    @abstractmethod
    def search(self, value: str):
        # Para buscar valores en tiempo real.
        raise NotImplementedError
    
    @abstractmethod
    def create(self, value: str):
        # Para crear valores.
        raise NotImplementedError