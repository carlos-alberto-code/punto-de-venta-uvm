import flet as ft

from controllers.products_controller import ProductController # Controlador de productos
from app.page.modules.content.inventory.__product_table import ProductTable # Tabla de productos
from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter # Barra de búsqueda y filtrado
from page.modules.content.inventory.top_buttons import AddNewButton, ShareButton # Botones de funcionalidad
from page.components.search_bar_filter.properties_controller import BrandFilter, CategoryFilter, UnitFilter # Filtros de búsqueda


class StockView(ft.Column):

    def __init__(self):
        super().__init__()
        self._product_controller = ProductController()
        self.products = self._product_controller.get_all()
        self.product_table = ProductTable(self.products)
        self.search_bar_filter = SearchBarFilter(
            Marca=BrandFilter(),
            Categoria=CategoryFilter(),
            Unidad=UnitFilter(),
        )
        self.share_button = ShareButton()
        self.add_button = AddNewButton()
        self.controls = [
            ft.Row(
                [self.search_bar_filter, ft.Row([self.share_button, self.add_button])],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            self.product_table,
        ]
