import flet as ft
from purchase_view.ItemList import ProductCard


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    # p = ProductCard(product=product, on_delete=lambda e: print("Delete"))

ft.app(main)