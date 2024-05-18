import flet as ft

from controllers.products_controller import ProductController
from page.modules.content.inventory.ProductTable import ProductTable
from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
from page.modules.content.inventory.top_buttons import AddNewButton, ShareButton
from page.components.search_bar_filter.properties_controller import UnitFilter, CategoryFilter, BrandFilter


class StockSection(ft.Column):
    # Responsable de formar la estructura de la sección de inventario
    def __init__(self):
        super().__init__()
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO
        self.controller = ProductController()
        products = self.controller.get_all()
        self.filter = SearchBarFilter(Categoria=CategoryFilter(), Marca=BrandFilter(), Unidad=UnitFilter())
        self.controls = [
            ft.Row( # SearchBarFilter, AddNewButton, ShareButton
                [self.filter, ft.Row([ShareButton(), AddNewButton()])],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ProductTable(products),
        ]