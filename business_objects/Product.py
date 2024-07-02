from business_objects.product_properties import Category, Brand, Unit


class Product:

    def __init__(
            self,
            product_id: int,
            unit_name: str,
            category_name: str,
            brand_name: str,
            quantity: int,
            cost_price: float,
            selling_price: float,
            reorder_level: int,
    ):
        self.product_id = product_id
        self.unit_name = unit_name
        self.category_name = category_name
        self.brand_name = brand_name
        self.quantity = quantity 
        self._cost_price = cost_price
        self.selling_price = selling_price
        self.reorder_level = reorder_level
    
    @property
    def name(self):
        return f'{self.brand_name} {self.unit_name}'
    
    @property
    def cost_price(self) -> float:
        return self._cost_price
    
    @property
    def total_cost(self) -> float:
        return round(self.quantity * self._cost_price, 2)
    
    @property
    def total_selling(self) -> float:
        return round(self.quantity * self.selling_price, 2)

    def __repr__(self) -> str:
        return f'Product(id={self.product_id}, name={self.name})'
