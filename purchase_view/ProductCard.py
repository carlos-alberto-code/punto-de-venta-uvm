import flet as ft
from classes.Product import Product


ft.Card()
class ProductCard(ft.Card): # Es la capa de presentación gráfica de un producto

    def __init__(self, product_description: str = 'None', existences: int = 0):
        super().__init__(
            content=ft.ListTile(
                leading=ft.Image(
                    src='https://images.pexels.com/photos/2983100/pexels-photo-2983100.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                    fit=ft.ImageFit.COVER,
                    border_radius=5,
                    filter_quality=ft.FilterQuality.HIGH,
                    
                ),
                title=ft.Text(f'{product_description}', size=13),
                subtitle=ft.Text(f'Existencias: {existences}', size=12),
                trailing=ft.IconButton(ft.icons.ADD),
                height=100,
            ),
            # width=300,
            # height=100,
        )
        