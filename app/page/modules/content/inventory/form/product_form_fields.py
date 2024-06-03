import flet as ft

from interfaces.interfaces import FieldInterface
from inventory.searchers import SimpleModelSearcher
from controllers.controllers import UnitController, CategoryController, BrandController

class UnitField(SimpleModelSearcher, FieldInterface):

    def __init__(self):
        SimpleModelSearcher.__init__(self, model_controller=UnitController())
        
    
    @property
    def value(self):
        pass

    def reset(self):
        pass