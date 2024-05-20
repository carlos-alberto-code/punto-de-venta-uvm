import flet as ft

from controllers.products_controller import ProductController
from page.modules.content.inventory.ProductTable import ProductTable
from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
from page.components.search_bar_filter.properties_controller import UnitFilter, CategoryFilter, BrandFilter
from page.modules.content.inventory.top_buttons import AddNewButton, ShareButton, FilterButton, SearchButton


class StockSection(ft.Column):
    # Responsable de formar la estructura de la sección de inventario
    def __init__(self):
        super().__init__(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.controller = ProductController()
        products = self.controller.get_all()
        self.product_table = ProductTable(products)
        self.filter = SearchBarFilter(Categoria=CategoryFilter(), Marca=BrandFilter(), Unidad=UnitFilter())
        self.controls = [
            # ft.Divider(),
            ft.Row( # SearchBarFilter, AddNewButton, ShareButton
                [
                    ft.Row(
                        [ft.Container(width=45), AddNewButton(), ShareButton()]
                    ),
                    ft.Row(
                        [self.filter, SearchButton(), ft.Container(width=45)]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            self.product_table,
        ]
        