from typing import Optional


class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f'Category(name={self.name})'
    
    
class Brand:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'Brand(name={self.name})'

class Unit:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'Unit(name={self.name})'


class Product:
    def __init__(
            self,
            id: Optional[int],
            unit: Unit,
            category: Category,
            brand: Brand,
            quantity: int,
            cost_price: float,
            selling_price: float,
            reorder_level: int,
    ) -> None:
        self.id = id
        self.unit = unit
        self.category = category
        self.brand = brand
        self.quantity = quantity
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.reorder_level = reorder_level
    
    @property
    def name(self):
        return f'{self.brand.name} {self.category.name}'
    
    def __repr__(self):
        return f'Product(name={self.name})'
    