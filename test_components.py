import flet as ft
from purchase_view.context import shape
from purchase_view.ItemList import ItemList
from purchase_view.ProductDTO import ProductDTO as Product


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    f = ItemList()
    page.add(f)
    f.add_item(Product(
        product_id=12,
        unit_name='Unidad',
        category_name='Categoría',
        brand_name='Marca',
        quantity=1,
        cost_price=10.0,
        selling_price=15.0,
        reorder_level=5
    ))
    f.add_item(Product(
        product_id=13,
        unit_name='Unidad',
        category_name='Categoría',
        brand_name='Marca',
        quantity=1,
        cost_price=10.0,
        selling_price=15.0,
        reorder_level=5
    ))
    page.update()


ft.app(main)