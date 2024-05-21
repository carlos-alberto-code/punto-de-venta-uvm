import flet as ft

from controllers.products_controller import ProductController
from page.modules.content.inventory.ProductTable import ProductTable
from page.modules.content.inventory.top_buttons import MenuOptionsButton
from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
from page.components.search_bar_filter.properties_controller import UnitFilter, CategoryFilter, BrandFilter


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
        self.filter = SearchBarFilter(
            table=self.product_table,
            product_controller=self.controller,
            Categoria=CategoryFilter(),
            Marca=BrandFilter(),
            Unidad=UnitFilter()
        )
        self.controls = [
            ft.Row( # SearchBarFilter, MenuOptionsButton, Container
                [
                    self.filter,
                    MenuOptionsButton(self.controller),
                    ft.Container(width=45),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            self.product_table,
        ]
        