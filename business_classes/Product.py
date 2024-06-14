from business_classes.product_properties import Category, Brand, Unit


class Product:

    def __init__(
            self,
            product_id: int,
            unit: Unit,
            category: Category,
            brand: Brand,
            quantity: int,
            cost_price: float,
            selling_price: float,
            reorder_level: int,
    ):
        self.product_id = product_id
        self.unit = unit
        self.category = category
        self.brand = brand
        self.quantity = quantity 
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.reorder_level = reorder_level
    
    @property
    def name(self):
        return f'Product({self.category.name}, {self.brand.name} {self.unit.name})'

    def __repr__(self) -> str:
        return f'Product(id={self.product_id}, name={self.name})'
