import flet as ft

from purchase_view.context import searcher, gird_view


def main(page: ft.Page):
    page.theme_mode             = ft.ThemeMode.LIGHT
    page.add(searcher, gird_view)

ft.app(target=main)