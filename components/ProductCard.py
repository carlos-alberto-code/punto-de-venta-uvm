import flet as ft
from business_classes.Product import Product


class ProductCard(ft.Card):

    SHAPE = ft.RoundedRectangleBorder(radius=20)
    TEXT_SIZE = 13

    def __init__(self, product: Product, on_button_click=None, on_card_click=None, on_long_press_card=None):
        super().__init__()
        self.shape = self.SHAPE
        self.data: Product = product
        self.content = ft.ListTile(
            leading=ft.Lottie(
                src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
                animate=True,
                repeat=False,
            ),
            title=ft.Text(product.name, size=self.TEXT_SIZE, weight=ft.FontWeight.BOLD),
            subtitle=ft.Column(
                controls=[
                    ft.Container(),
                    ft.Text(f'Precio de venta: {product.selling_price:,.2f} MXN', size=self.TEXT_SIZE),
                    ft.Text(f'Existencias: {product.quantity}', size=self.TEXT_SIZE),
                ],
            ),
            trailing=ft.IconButton(
                icon=ft.icons.ADD,
                on_click=on_button_click,
            ),
            toggle_inputs=True,
            shape=self.SHAPE,
            on_click=on_card_click,
            on_long_press=on_long_press_card,
        )