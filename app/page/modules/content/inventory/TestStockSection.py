import flet as ft

from .product_detail import ProductDetail
from .top_buttons import AddNewButton, ShareButton
from .ProductTable import ProductTable, create_column
from controllers.products_controller import ProductController
from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter


prod = ProductController().get_by_id(1)

class TestStockSection(ft.Row):

    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            SearchBarFilter(),
                            ft.Row(
                                controls=[
                                    ShareButton(),
                                    AddNewButton(),
                                ]
                            )
                        ]
                    ),
                    ProductTable()
                ]
            ),
            ProductDetail(product=prod),
        ]