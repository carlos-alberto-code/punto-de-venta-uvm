import flet as ft

from page.components.interfaces.SearcherControllerInterface import SearcherControllerInterface
from page.modules.content.inventory.ProductTable import ProductTable


ft.SearchBar()
class ProductSearcher(ft.SearchBar):

    def __init__(self, product_controller: SearcherControllerInterface, product_table: ProductTable):
        super().__init__(
            width=300,
            height=40,
            bar_leading=ft.Icon(str(ft.icons.SEARCH)),
            view_leading=ft.Icon(str(ft.icons.SEARCH)),
            bar_hint_text='Buscar producto',
            on_tap=self.reset,
            on_change=self.update_table
        )
        self.controller = product_controller
        self.table = product_table
    
    def reset(self, event: ft.ControlEvent):
        self.close_view(event.data)
        self.table.products = self.controller.get_all()
        self.table.update()

    def update_table(self, event: ft.ControlEvent):
        instances = self.controller.search(event.data)
        self.table.products = instances
        self.table.update()
        