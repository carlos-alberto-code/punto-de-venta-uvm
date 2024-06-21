import flet as ft
from store_view.ProductDTO import ProductDTO as Product # Data Transfer Object


ft.Card()
class ProductCard(ft.Card): # Es la capa de presentación gráfica de un producto

    def __init__(self, product: Product, on_click=None):
        super().__init__(
            content=ft.ListTile(
                leading=ft.Icon(ft.icons.SHOPPING_CART, size=30),
                title=ft.Text(f'{product.name}', size=13),
                subtitle=ft.Text(f'Existencias: {product.quantity}', size=12),
                trailing=ft.IconButton(ft.icons.ADD, on_click=on_click, data=product),
                height=100,
            ),
            
        )
        