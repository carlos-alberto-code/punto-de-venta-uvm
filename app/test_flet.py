import flet as ft
from page.modules.content.inventory.stock_section import Filter


def main(page: ft.Page):
    f = Filter()
    page.add(f)

ft.app(target=main)