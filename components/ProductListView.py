import flet as ft
from business_classes.Product   import Product
from components.ProductCard     import ProductCard


class ProductListView(ft.ListView):

    def __init__(self, on_add_button_click=None, on_card_button_click=None, on_long_press_card=None, col=8):
        super().__init__()
        self.col = col
        self.controls: list[ProductCard] = []
        self.data: list[Product] | None
        self.on_add_button_click = on_add_button_click
        self.on_card_button_click = on_card_button_click
        self.on_long_press_card = on_long_press_card
    
    @property
    def products(self) -> list[Product] | None:
        return self.data
    
    @products.setter
    def products(self, products: list[Product] | None) -> None:
        self.data = products
        self._charge_product_cards()
    
    def _charge_product_cards(self) -> None:
        if self.data:
            self.controls.clear()
            for product in self.data:
                card = ProductCard(
                    product=product,
                    on_button_click=self.on_add_button_click,
                    on_card_click=self.on_card_button_click,
                    on_long_press_card=self.on_long_press_card
                )
                self.controls.append(card)