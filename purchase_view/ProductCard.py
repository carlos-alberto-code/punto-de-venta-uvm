import flet as ft
from business_classes.Product import Product as Product # Data Transfer Object


ft.Card()
class ProductCard(ft.Card): # Es la capa de presentación gráfica de un producto

    def __init__(self, product: Product, on_click=None):
        super().__init__(
            content=ft.ListTile(
                leading=ft.Image(
                    src='https://images.pexels.com/photos/2983100/pexels-photo-2983100.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                    fit=ft.ImageFit.COVER,
                    border_radius=5,
                    filter_quality=ft.FilterQuality.HIGH,
                    
                ),
                title=ft.Text(f'{product.name}', size=13),
                subtitle=ft.Text(f'Existencias: {product.quantity}', size=12),
                trailing=ft.IconButton(ft.icons.ADD, on_click=on_click, data=product),
                height=100,
            ),
        )
        