import flet as ft
from datetime                   import datetime
from components.product_cards   import ProductCard
from components.ProductList     import ProductList


class ShoppingCart(ft.Card):

    BUTTON_STYLE = ft.ButtonStyle(shape={'': ft.RoundedRectangleBorder(radius=8)})

    def __init__(
            self,
            title: str = 'Carrito de compras',
            icon: str = 'shopping_cart',
            on_clear_button_click=None,
    ):
        super().__init__(expand=True)

        self.date               = datetime.now().date()
        self.time               = datetime.now().time()

        self._product_list_view  = ProductList()

        self.top_controls = [
            ft.Row([ft.Icon(icon, size=30)], alignment=ft.MainAxisAlignment.CENTER),
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
                ft.ElevatedButton('Limpiar', expand=True, style=self.BUTTON_STYLE, on_click=on_clear_button_click),
                ft.ElevatedButton('Calcular', expand=True, style=self.BUTTON_STYLE),
                ft.ElevatedButton('Guardar', expand=True, style=self.BUTTON_STYLE),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    *self.top_controls,
                    ft.Divider(),
                    self._product_list_view,
                    ft.Divider(),
                    self.total_text,
                    self.actions
                ],
            ),
            padding=10,
        )
    
    @property
    def product_list_view(self) -> ProductList:
        return self._product_list_view
    
    def add_product_card(self, product_card: ProductCard):
        self._product_list_view.add_product_card(product_card)

    def remove_product_card(self, product_card: ProductCard):
        self._product_list_view.remove_product_card(product_card)

    def clear_product_list_cards(self):
        self._product_list_view.clear_product_cards() 
