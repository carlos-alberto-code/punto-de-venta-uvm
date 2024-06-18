import flet as ft
from purchase_view.purchase_form import PurchaseForm, ProductFormCard
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

    form = PurchaseForm()
    card = ProductFormCard(product)

    page.add(
        card
    )
    # form.add_item(product=product)
    # page.update()

ft.app(main)