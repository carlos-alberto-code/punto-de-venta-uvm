import flet as ft
from purchase_view.ItemList import WidgetItemList
from purchase_view.ProductDTO import ProductDTO as Product


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    l = WidgetItemList('Lista de Compras')
    page.add(l)
    l.add_product(
        product=Product(
            product_id=1,
            unit_name='Caja',
            category_name='Frutas',
            brand_name='La Costeña',
            quantity=2,
            cost_price=255.92,
            selling_price=30.0,
            reorder_level=10,
        )
    )
    l.add_product(
        product=Product(
            product_id=2,
            unit_name='kg',
            category_name='Frutas',
            brand_name='Del Monte',
            quantity=2,
            cost_price=25.0,
            selling_price=30.0,
            reorder_level=10,
        )
    )
    l.add_product(
        product=Product(
            product_id=3,
            unit_name='Pieza',
            category_name='Agua',
            brand_name='Ciel',
            quantity=2,
            cost_price=10.80,
            selling_price=30.0,
            reorder_level=10,
        )
    )
    l.add_product(
        product=Product(
            product_id=4,
            unit_name='Pieza',
            category_name='Agua',
            brand_name='Bonafont',
            quantity=2,
            cost_price=10.80,
            selling_price=30.0,
            reorder_level=10,
        )
    )
    l.add_product(
        product=Product(
            product_id=5,
            unit_name='Pieza',
            category_name='Agua',
            brand_name='Ciel',
            quantity=2,
            cost_price=10.80,
            selling_price=30.0,
            reorder_level=10,
        )
    )
    page.update()

ft.app(main)