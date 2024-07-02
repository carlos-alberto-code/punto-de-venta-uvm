from business_objects.Product   import Product


class SaleDetail:
    def __init__(
            self,
            product:            Product,
            quantity:           int,
    ) -> None:
        self._product: Product   = product
        self._quantity           = quantity
    
    @property
    def unit_price(self) -> float:
        return self._product.selling_price
    
    @property
    def total_price(self) -> float:
        return self.unit_price * self._quantity
    
    @property
    def product(self) -> Product:
        return self._product
    
    @property
    def quantity(self) -> int:
        return self._quantity
    