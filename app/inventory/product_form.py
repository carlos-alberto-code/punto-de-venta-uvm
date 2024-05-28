# Componentes
from naveasy.forms import AlertForm
from app.naveasy.components.counters import Counter
from app.naveasy.components.searchers import SimpleModelSearcher
# Interfaces
from naveasy.interfaces import FieldInterface as Field
from naveasy.interfaces import ControllerInterface as ControllerInterface

from inventory.inventory_controllers import ProductController, UnitController, BrandController, CategoryController


class BrandSearcher(Field, SimpleModelSearcher):
        
    def __init__(self, controller: ControllerInterface):
        super().__init__(controller)

    def reset(self):
        self.bar_hint_text = 'Se ha reseteado el campo'
        self.update()


class UnitSearcher(Field, SimpleModelSearcher):
    
    def __init__(self, controller: ControllerInterface):
        super().__init__(controller)

    def reset(self):
        self.bar_hint_text = 'Se ha reseteado el campo'
        self.update()


class CategorySearcher(Field, SimpleModelSearcher):
    
    def __init__(self, controller: ControllerInterface):
        super().__init__(controller)

    def reset(self):
        self.bar_hint_text = 'Se ha reseteado el campo'
        self.update()


class QuantityCounter(Field, Counter):
    
    def __init__(self):
        super().__init__()

    def reset(self):
        self.value = 666
        self.update()


class CostCounter(Field, Counter):
    
    def __init__(self):
        super().__init__()

    def reset(self):
        self.value = 666
        self.update()


class PriceCounter(Field, Counter):
        
    def __init__(self):
        super().__init__()

    def reset(self):
        self.value = 666
        self.update()


class ReorderCounter(Field, Counter):
    
    def __init__(self):
        super().__init__()

    def reset(self):
        self.value = 666
        self.update()


ProductForm = AlertForm(
    title='Nuevo producto',
    model_controller=ProductController(),
    Unidad=UnitSearcher(UnitController()),
    Categoria=CategorySearcher(CategoryController()),
    Marca=BrandSearcher(BrandController()),
    Cantidad=QuantityCounter(),
    Costo=CostCounter(),
    Precio=PriceCounter(),
    Reorden=ReorderCounter(),
)