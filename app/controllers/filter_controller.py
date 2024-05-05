from abc import ABC, abstractmethod
from models.models import Unit, Category, Brand
from database.connection import get_db


class FilterController(ABC):
    # Esta será una interfaz que debrán usar ciertos controladores 
    # para que se pueda implementar la funcionalidad de filtrado y búsqueda.

    @abstractmethod
    def get_all_values(self):
        # Para obtener todos los valores de la tabla que implementa el controlador.
        raise NotImplementedError

    @abstractmethod
    def search(self, value: str):
        # Para buscar valores en la tabla que implementa el controlador.
        raise NotImplementedError
    
    @abstractmethod
    def get_property_name(self):
        # Para obtener el nombre de la propiedad que se está filtrando.
        raise NotImplementedError


class UnitsController(FilterController):
    pass


class CategoriesController(FilterController):
    pass


class BrandsController(FilterController):
    pass
