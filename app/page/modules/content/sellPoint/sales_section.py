import flet as ft
import sys
sys.path.append('..')
from controllers.inventory_controller import InventoryController

_search_bar = ft.TextField(
    label='Buscar',
)
class SalesSection(ft.Column):
    def __init__(self):
        super().__init__()
        self.products = InventoryController().get_all()
        self.controls = [
            ft.Row(
                controls=[
                    ft.Card(
                        content= ft.Container(
                            content= ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Image(
                                                src=f"https://picsum.photos/200/200?{self.products.index(product)}",
                                                width=200,
                                                height=200,
                                                border_radius=ft.border_radius.all(10)),
                                        ]
                                    ),
                                    ft.Column(
                                        [   
                                            ft.Text(f"Producto {self.products.index(product)+1}", weight=ft.FontWeight.BOLD),
                                            ft.Text(product.description),
                                            ft.Text(f"$ {str(product.sale_price)}"),
                                        ]
                                    ),
                                    ft.Column(
                                        [
                                            ft.TextButton('Agregar al carrito')
                                        ]
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                wrap= True
                            ),
                            width=700,
                            padding=10,
                        ),
                    )for product in self.products
                ],
                wrap=True,
                spacing=10,
                run_spacing=10,
            )
        ]