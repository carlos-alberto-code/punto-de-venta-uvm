import flet as ft

from controllers.products_controller import ProductController
from page.modules.content.inventory.product_detail import ProductDetail
from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
from page.modules.content.inventory.top_buttons import AddNewButton, ShareButton
from page.components.search_bar_filter.properties_controller import BrandFilter, CategoryFilter, UnitFilter


class StockView(ft.Row):

    def __init__(self):
        super().__init__()
        self.product_controller = ProductController()
        product = self.product_controller.get_by_id(1)
        self.search_bar_filter: ft.SearchBar = SearchBarFilter(
            Marca=BrandFilter(),
            Categoria=CategoryFilter(),
            Unidad=UnitFilter(),
        )
        self.share_button: ft.PopupMenuButton = ShareButton()
        self.add_button: ft.ElevatedButton = AddNewButton()
        self.product_views: ft.Tabs
        self.product_detail: ft.Card = ProductDetail(product=product)
        self.controls = [
            ft.Column( # Para los controles de funcionalidad y los productos
                controls=[
                    ft.Row(# Para el filtrador y los íconos de exportación y registro
                        controls=[
                            self.search_bar_filter, # Buscador y Filtrador
                            ft.Row(
                                controls=[
                                    self.share_button,
                                    self.add_button,
                                ]
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN # Para separarlos
                    ),
                    ft.Row( # Para la muestra de productos
                        controls=[
                            # self.product_views,
                        ]
                    )
                ]
            ),
            ft.Column( # Para mostrar el producto a detalle
                controls=[ # Sólo requiere un control general
                    self.product_detail,
                ]
            )
        ]
