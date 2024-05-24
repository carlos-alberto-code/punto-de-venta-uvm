import flet as ft

from controllers.products_controller import ProductController
from page.modules.content.inventory.ProductTable import ProductTable


class ProductSearcher(ft.SearchBar):

    def __init__(self, product_controller: ProductController, product_table: ProductTable):
        super().__init__(
            width=300,
            height=40,
            bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
            bar_hint_text='Buscar producto',
            tooltip='Clic para restaruar la tabla de productos',
            on_tap=self.reset,
            on_change=self.update_table,
        )
        self.table = product_table
        self.controller = product_controller
    
    def reset(self, event: ft.ControlEvent):
        self.close_view(event.data)
        self.table.products = self.controller.get_all()
        self.table.update()

    def update_table(self, event: ft.ControlEvent):
        instances = self.controller.search_products(event.data)
        self.table.products = instances
        self.table.update()
        