import flet as ft
from purchase_view.ProductViewCard import ProductViewCard
from business_classes.Product import Product # Data Transfer Object


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    product = Product(
        product_id=1,
        unit_name='600 ml',
        category_name='Bebida',
        brand_name='Fuze Tea',
        quantity=10,
        cost_price=23.12,
        selling_price=29.99,
        reorder_level=5,
    )

    p2 = Product(
        product_id=2,
        unit_name='355 ml',
        category_name='Bebida',
        brand_name='Coca Cola',
        quantity=10,
        cost_price=15.99,
        selling_price=29.99,
        reorder_level=5,
    )

    p3 = Product(
        product_id=3,
        unit_name='Bolsa',
        category_name='Papas',
        brand_name='Sabritas',
        quantity=10,
        cost_price=12.23,
        selling_price=29.99,
        reorder_level=5,
    )

    pv1 = ProductViewCard(product)
    pv2 = ProductViewCard(p2)
    pv3 = ProductViewCard(p3)
    page.add(pv1, pv2, pv3)




ft.app(main)