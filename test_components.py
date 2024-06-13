import flet as ft
from purchase_view.widget_item_cards import WidgetItemCard
from purchase_view.ProductDTO import ProductDTO as Product # Data Transfer Object


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(WidgetItemCard(Product(
        product_id=1,
        unit_name='Pieza',
        category_name='Refresco',
        brand_name='Coca-Cola',
        quantity=10,
        cost_price=22.50,
        selling_price=33.90,
        reorder_level=5,
    )))


ft.app(main)