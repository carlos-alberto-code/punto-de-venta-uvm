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
            on_calculate_button_click=None,
            on_process_button_click=None,
    ):
        super().__init__(expand=True)

        self._date               = datetime.now().date()
        self._time               = datetime.now().time()

        self._product_list_view  = ProductList()

        self.top_controls = [
            ft.Row([ft.Icon(icon, size=30)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Text(title, size=21)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Text(f'{self._date}')], alignment=ft.MainAxisAlignment.CENTER),
        ]
        self._total_text_value:ft.Text = ft.Text(f'Total: {0:,.2f} MXN', size=18)
        self.row_shape = ft.Row(
            controls=[
                self._total_text_value,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self.actions = ft.Row(
            [
                ft.ElevatedButton('Limpiar', expand=True, style=self.BUTTON_STYLE, on_click=on_clear_button_click),
                ft.ElevatedButton('Calcular', expand=True, style=self.BUTTON_STYLE, on_click=on_calculate_button_click),
                ft.ElevatedButton('Procesar', expand=True, style=self.BUTTON_STYLE, on_click=on_process_button_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    *self.top_controls,
                    ft.Divider(),
                    self._product_list_view,
                    ft.Divider(),
                    self.row_shape,
                    self.actions
                ],
            ),
            padding=10,
        )
        self._total_selling = 0.0
    
    @property
    def total_selling(self) -> float:
        return self._total_selling
    
    @total_selling.setter
    def total_selling(self, value: float):
        self._total_selling = value
    
    @property
    def date(self):
        return self._date
    
    @property
    def time(self):
        return self._time.strftime('%H:%M')
    
    @property
    def product_list_view(self) -> ProductList:
        return self._product_list_view
    
    @property
    def total_text_value(self) -> float | str | None:
        return self._total_text_value.value
    
    @total_text_value.setter
    def total_text_value(self, value: float):
        self._total_text_value.value = f'Total: {value:,.2f} MXN'
        self.total_selling = value
    
    @property
    def number_of_items(self) -> int:
        return self._product_list_view.number_of_product_cards
    
    def add_product_card(self, product_card: ProductCard):
        self._product_list_view.add_product_card(product_card)

    def remove_product_card(self, product_card: ProductCard):
        self._product_list_view.remove_product_card(product_card)

    def clear_all_cards(self):
        self._product_list_view.clear_product_cards() 
