import flet as ft
from classes.Product import Product


ft.Card()
class ProductCard(ft.Card): # Es la capa de presentación gráfica de un producto

    def __init__(self):
        super().__init__(
            content=ft.ListTile(
                leading=ft.Image(
                    src='https://images.pexels.com/photos/3270223/pexels-photo-3270223.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                    fit=ft.ImageFit.COVER,
                    border_radius=10,
                    filter_quality=ft.FilterQuality.HIGH,
                    
                ),
                title=ft.Text('Coca-Cola 355 ml', size=13),
                subtitle=ft.Text('Existencias: 10', size=12),
                trailing=ft.IconButton(ft.icons.ADD),
            ),
            width=300,
            elevation=5,
        )
        