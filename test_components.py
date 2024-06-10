import flet as ft

from purchase_view.context import searcher


def main(page: ft.Page):
    page.theme_mode             = ft.ThemeMode.LIGHT
    page.add(searcher)

ft.app(target=main)