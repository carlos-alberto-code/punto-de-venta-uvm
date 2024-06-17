import flet as ft
from purchase_view.context import shape
from purchase_view.ItemList import ItemSet, WidgetPurchaseList
from purchase_view.ProductDTO import ProductDTO as Product


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(WidgetPurchaseList())


ft.app(main)