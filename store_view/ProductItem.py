import flet as ft
from store_view.ProductDTO import ProductDTO as Product # Data Transfer Object
from components.counters import Counter


ft.Card()
class ProductItem(ft.Card): # Es la capa de presentación gráfica de un producto

    def __init__(self, product: Product, on_click=None):
        super().__init__(

        )
        self.counter = Counter()
        self.content=ft.ListTile(
                leading=ft.Image(
                    src='https://images.pexels.com/photos/2983100/pexels-photo-2983100.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                    fit=ft.ImageFit.COVER,
                    border_radius=5,
                    filter_quality=ft.FilterQuality.HIGH,
                    
                ),
                title=ft.Text(f'{product.name}', size=13),
                subtitle=ft.Row(
                        [
                            ft.Text(value=f'Precio: ${product.cost_price}', size=12),
                            self.counter,
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),   
                trailing=ft.IconButton(ft.icons.DELETE, on_click=on_click, data=product),
                height=100,
            )