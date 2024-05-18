import sys

sys.path.append('app/')


import flet as ft

from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
from controllers.products_controller import ProductController
from app.page.modules.content.inventory.__product_table import ProductTable

controller = ProductController()
products = controller.get_all()
products = products[:30]

pt = ProductTable(products)



def main(page: ft.Page):
    # page.scroll = ft.ScrollMode.HIDDEN
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(ft.Column(
        [pt], scroll=ft.ScrollMode.AUTO, expand=True
    ))

ft.app(target=main)