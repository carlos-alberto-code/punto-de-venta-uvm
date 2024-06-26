import flet as ft
from business_classes.Product   import Product
from components.ProductCard     import ProductCard


class ProductListView(ft.ListView):

    def __init__(self):
        super().__init__()
        self.controls: list[ProductCard] = []
        self.data: list[Product]
    
    @property
    def products(self) -> list[Product] | None:
        return self.data
    
    @products.setter
    def products(self, products: list[Product]) -> None:
        self.data = products
        self._charge_product_cards()
    
    def _charge_product_cards(self) -> None:
        for product in self.data:
            card = ProductCard(product=product)
            self.controls.append(card)