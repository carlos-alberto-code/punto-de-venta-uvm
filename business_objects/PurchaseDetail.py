from business_objects.Product import Product

class PurchaseDetail:
    def __init__(self, product: Product, quantity: int, unit_purchase_price: float) -> None:
        self._product = product
        self._quantity = quantity
        self._unit_purchase_price = unit_purchase_price

    @property
    def unit_purchase_price(self) -> float:
        return self._unit_purchase_price

    @property
    def total_purchase_price(self) -> float:
        return self._unit_purchase_price * self._quantity

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity