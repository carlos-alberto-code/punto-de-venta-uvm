import flet as ft
from datetime                   import datetime

from business_classes.Product   import Product
from components.ProductList     import ProductList
from components.product_cards   import ProductCardFactory, CardType


class ShoppingCart(ft.Card):

    BUTTON_STYLE = ft.ButtonStyle(shape={'': ft.RoundedRectangleBorder(radius=8)})

    def __init__(self, title: str = 'Carrito de compras'):
        super().__init__(expand=True)

        self.date               = datetime.now().date()
        self.card_factory       = ProductCardFactory()
        self.product_list_view  = ProductList()

        self.top_controls = [
            ft.Row([ft.Text(title, size=21)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Text(f'{self.date}')], alignment=ft.MainAxisAlignment.CENTER),
        ]
        self.total_value = 0.00
        self.total_text = ft.Row(
            controls=[
                ft.Text(f'Total: {self.total_value:,.2f} MXN', size=18)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.actions = ft.Row(
            [
                ft.ElevatedButton('Limpiar', expand=True, style=self.BUTTON_STYLE, on_click=self.handler_on_clear_click),
                ft.ElevatedButton('Calcular', expand=True, style=self.BUTTON_STYLE, on_click=self.handler_on_calculate_click),
                ft.ElevatedButton('Guardar', expand=True, style=self.BUTTON_STYLE),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    *self.top_controls,
                    ft.Divider(),
                    self.product_list_view,
                    ft.Divider(),
                    self.total_text,
                    self.actions
                ],
            ),
            padding=10,
        )
    
    def add_product(self, product: Product):
        card = self.card_factory.create_product_card(
            product=product,
            card_type=CardType.SELLING,
            on_button_card_click=self.handler_on_button_card_click,
        )
        self.product_list_view.add_product_card(card)
        self.product_list_view.update()
    
    def handler_on_clear_click(self, event: ft.ControlEvent):
        self.product_list_view.clear_product_cards()
        self.product_list_view.update()
    
    def handler_on_button_card_click(self, event: ft.ControlEvent):
        button = event.control
        self.product_list_view.remove_product_card(button.data)
        self.product_list_view.update()

    def handler_on_calculate_click(self, event: ft.ControlEvent):
        self.total_value = sum([card.get_total_card for card in self.product_list_view.product_cards]) # type: ignore
        self.total_text.controls[0] = ft.Text(f'Total: ${self.total_value:,.2f} MXN', size=18)
        self.total_text.update()
