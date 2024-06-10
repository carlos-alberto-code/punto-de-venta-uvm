import flet as ft

from purchase_view.ProductCard import ProductCard


def main(page: ft.Page):
    page.theme_mode             = ft.ThemeMode.LIGHT

    page.add(ProductCard(), ProductCard(), ProductCard())

ft.app(target=main)