import flet as ft
from business_classes.Product import Product
from components.counters import IntCounter
from components.EditableField import EditableField


TEXT_SIZE = 13

class ProductCard(ft.Card):

    SHAPE = ft.RoundedRectangleBorder(radius=20)

    def __init__(
            self,
            product: Product,
            on_button_card_click=None,
            on_card_click=None,
            on_long_press_card=None,
    ):
        super().__init__()
        self.shape = self.SHAPE
        self.data: Product = product
        self._subtitle: ft.Column = ft.Column(
            controls=[ft.Container()],
            spacing=0,
        )
        self.content:ft.ListTile = ft.ListTile(
            data=self.data,
            leading=ft.Lottie(
                src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
                animate=True,
                repeat=False,
            ),
            title=ft.Text(f'{product.name}', size=TEXT_SIZE, weight=ft.FontWeight.BOLD),
            toggle_inputs=True,
            shape=self.SHAPE,
            on_click=on_card_click,
            on_long_press=on_long_press_card,
        )


class DisplayProductCard(ProductCard):

    def __init__(self, product: Product, on_button_card_click=None, on_card_click=None, on_long_press_card=None):
        super().__init__(product, on_button_card_click, on_card_click, on_long_press_card)
        display_controls = [
            ft.Text(f'Precio de venta: {product.selling_price:,.2f} MXN', size=TEXT_SIZE),
            ft.Text(f'Existencias: {product.quantity}', size=TEXT_SIZE),
        ]
        
        self._subtitle.controls += display_controls
        self.content.subtitle = self._subtitle
        self.content.trailing = ft.IconButton(
            icon=ft.icons.ADD,
            on_click=on_button_card_click,
            data=self.data,
        )
    

class SellingProductCard(ProductCard):

    def __init__(self, product: Product, on_button_card_click=None, on_card_click=None, on_long_press_card=None):
        super().__init__(product, on_button_card_click, on_card_click, on_long_press_card)
        self.counter = IntCounter(
            start_value=int(1),
            readonly=False,
            on_counter_change=self.handler_on_counter_change,
        )
        display_controls = [
            ft.Text(f'Precio de venta: {product.selling_price:,.2f} MXN', size=TEXT_SIZE),
            ft.Row(
                [
                    ft.Text('Cantidad: ', size=TEXT_SIZE),
                    self.counter,
                ]
            ),
            ft.Text(f'Precio total: {product.selling_price * int(self.counter.value):,.2f} MXN', size=TEXT_SIZE),
        ]
        self._subtitle.controls += display_controls
        self.content.subtitle = self._subtitle
        self.content.trailing = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=on_button_card_click,
            data=self.data,
        )
    
    def handler_on_counter_change(self, event: ft.ControlEvent):
        total_selling = int(self.counter.value) * self.data.selling_price
        self._subtitle.controls[-1] = ft.Text(f'Precio total: {total_selling:,.2f} MXN', size=TEXT_SIZE)
        self.content.update()


class PurchaseProductCard(ProductCard):

    def __init__(self, product: Product, on_button_card_click=None, on_card_click=None, on_long_press_card=None):
        super().__init__(product, on_button_card_click, on_card_click, on_long_press_card)
        self.int_counter = IntCounter(
            start_value=1,
            readonly=False,
            on_counter_change=self.handler_on_counter_change,
        )
        self.editable_field = EditableField(
            text_size=TEXT_SIZE,
            prefix_text='Costo de compra: $',
            value=product.cost_price,
            suffix_text='MXN',
            on_submit=self.handler_on_field_submit,
            # Permitir sólo dos números decimales
            input_filter=r'^\d{1,6}(\.\d{0,2})?$',
        )
        display_controls = [
            self.editable_field,
            ft.Row(
                [
                    ft.Text('Cantidad: ', size=TEXT_SIZE),
                    self.int_counter,
                ]
            ),
            ft.Text(f'Costo total: {product.cost_price * int(self.int_counter.value):,.2f} MXN', size=TEXT_SIZE),
        ]
        self._subtitle.controls += display_controls
        self.content.subtitle = self._subtitle
        self.content.trailing = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=on_button_card_click,
            data=self.data,
        )
    
    def handler_on_counter_change(self, event: ft.ControlEvent):
        if self.editable_field.get_value:
            total_purchase = float(self.editable_field.get_value) * int(self.int_counter.value)
            self._subtitle.controls[-1] = ft.Text(f'Costo total: {total_purchase:,.2f} MXN', size=TEXT_SIZE)
            self.content.update()

    def handler_on_field_submit(self, event: ft.ControlEvent):
        field = event.control
        total = float(field.value) * int(self.int_counter.value)
        self._subtitle.controls[-1] = ft.Text(f'Costo total: {total:,.2f} MXN', size=TEXT_SIZE)
        self.content.update()
        