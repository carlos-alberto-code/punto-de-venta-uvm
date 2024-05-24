import flet as ft

from page.components.ProductSearcher             import ProductSearcher
from controllers.products_controller             import ProductController
from page.modules.content.inventory.ProductTable import ProductTable
from page.modules.content.inventory.top_buttons  import OptionsMenuButton


class StockSection(ft.Column):
    # Responsable de formar la estructura de la sección de inventario
    def __init__(self):
        super().__init__(
            expand=True,
            # scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.controller = ProductController()
        products = self.controller.get_all()
        self.product_table = ProductTable(products)
        self.product_searcher = ProductSearcher(self.controller, self.product_table)
        self.controls = [
            ft.Row( # SearchBarFilter, MenuOptionsButton, Container
                [   
                    
                    # Searcher('Productos', BrandFilter()),
                    self.product_searcher,
                    OptionsMenuButton(),
                    ft.Container(width=45)
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            ft.Column(
                [
                    self.product_table,
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )
        ]
        