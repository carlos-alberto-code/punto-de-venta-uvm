import flet as ft
from business_classes.Product import Product # Data Transfer Object


class ProductViewCard(ft.Card):
    def __init__(self, product: Product, on_add=None):
        super().__init__(
            width=250,
        )
        self.product = product
        self.on_add = on_add
        self.content = self.create_content()
    
    def create_content(self):
        return ft.ListTile(
            leading=ft.Icon(ft.icons.SHOPPING_CART, size=30),
            title=ft.Text(self.product.name),
            subtitle=ft.Text(f'Existencias: {self.product.quantity}'),
            trailing=ft.IconButton(icon=ft.icons.ADD, on_click=self.on_add),
        )