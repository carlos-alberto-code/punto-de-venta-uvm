# TODO: Desacoplar los calculos del producto en sí y dejarlo todo en los componentes.

import flet as ft
from enum import Enum

from business_objects.Product import Product
from components.counters      import IntCounter
from components.EditableField import EditableField


TEXT_SIZE = 13

class ProductCard(ft.Card):

    SHAPE = ft.RoundedRectangleBorder(radius=20)

    def __init__(
            self,
            product: Product,
            on_button_card_click=None,
    ):
        super().__init__()
        self.shape = self.SHAPE
        self._product = product
        self.data = {
            'product': product,
            'card': self,
        }
        self._subtitle: ft.Column = ft.Column(
            controls=[ft.Container()],
            spacing=0,
        )
        self.content:ft.ListTile = ft.ListTile(
            data=product,
            leading=ft.Lottie(
                src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
                animate=True,
                repeat=False,
            ),
            title=ft.Text(f'{product.name}', size=TEXT_SIZE, weight=ft.FontWeight.BOLD),
            shape=self.SHAPE,
        )
    
    @property
    def product(self) -> Product:
        return self._product
    
    @property
    def get_total_card(self) -> float | str | None:
        pass

    @property
    def quantity(self) -> int:
        return 0


class DisplayProductCard(ProductCard):

    def __init__(self, product: Product, on_button_card_click=None):
        super().__init__(product, on_button_card_click)
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

    def __init__(self, product: Product, on_button_card_click=None):
        super().__init__(product, on_button_card_click)
        self.counter = IntCounter(
            start_value=1,
            readonly=False,
            end_value=product.quantity,
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
        # Si el valor del campo es mayor que el valor final, hacer el calculo sólo hasta el valor final
        if  not int(self.counter.value) > self.data['product'].quantity: # type: ignore
            total_selling = int(self.counter.value) * self.data['product'].selling_price # type: ignore
            self._subtitle.controls[-1] = ft.Text(f'Precio total: {total_selling:,.2f} MXN', size=TEXT_SIZE)
            self.content.update()
    
    @property
    def get_total_card(self) -> float | str | None:
        return self.data['product'].selling_price * int(self.counter.value) # type: ignore

    @property
    def quantity(self):
        return int(self.counter.value)


class PurchaseProductCard(ProductCard):

    def __init__(self, product: Product, on_button_card_click=None):
        super().__init__(product, on_button_card_click)
        self.int_counter = IntCounter(
            start_value=1,
            readonly=False,
            on_counter_change=self.handler_on_counter_change,
        )
        self._editable_field = EditableField(
            text_size=TEXT_SIZE,
            prefix_text='Costo de compra: $',
            value=product._cost_price,
            suffix_text='MXN',
            on_submit=self.handler_on_field_submit,
            input_filter=r'^\d{1,6}(\.\d{0,2})?$',
        )
        display_controls = [
            self._editable_field,
            ft.Row(
                [
                    ft.Text('Cantidad: ', size=TEXT_SIZE),
                    self.int_counter,
                ]
            ),
            ft.Text(f'Costo total: {product._cost_price * int(self.int_counter.value):,.2f} MXN', size=TEXT_SIZE),
        ]
        self._subtitle.controls += display_controls
        self.content.subtitle = self._subtitle
        self.content.trailing = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=on_button_card_click,
            data=self.data,
        )
    
    def handler_on_counter_change(self, event: ft.ControlEvent):
        if self._editable_field.get_value:
            total_purchase = float(self._editable_field.get_value) * int(self.int_counter.value)
            self._subtitle.controls[-1] = ft.Text(f'Costo total: {total_purchase:,.2f} MXN', size=TEXT_SIZE)
            self.content.update()

    def handler_on_field_submit(self, event: ft.ControlEvent):
        field = event.control
        total = float(field.value) * int(self.int_counter.value)
        self._subtitle.controls[-1] = ft.Text(f'Costo total: {total:,.2f} MXN', size=TEXT_SIZE)
        self.content.update()
    
    
    @property
    def editable_field(self) -> EditableField:
        return self._editable_field
    
    @property
    def cost_price(self) -> float | None:
        if self.editable_field.get_value:
            return float(self.editable_field.get_value)
    
    @property
    def get_total_card(self) -> float | str | None:
        return float(self._editable_field.get_value) * int(self.int_counter.value) # type: ignore
    
    @property
    def quantity(self):
        return int(self.int_counter.value)


class CardType(Enum):
    DISPLAY = 'display'
    SELLING = 'selling'
    PURCHASE = 'purchase'


class ProductCardFactory:

    def __init__(self):
        self._product_cards = {
            CardType.DISPLAY:   DisplayProductCard,
            CardType.SELLING:   SellingProductCard,
            CardType.PURCHASE:  PurchaseProductCard,
        }

    def create_product_card(self, product: Product, card_type: CardType, **kwargs):
        return self._product_cards[card_type](product, **kwargs)
    