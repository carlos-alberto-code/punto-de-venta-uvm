import flet as ft

from purchase_view.context import searcher, gird_view, product_form


def main(page: ft.Page):
    page.theme_mode             = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.add(product_form, searcher, gird_view)

ft.app(target=main)