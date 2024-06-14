from typing import Optional
import flet as ft
from datetime import datetime as dt

from components.counters import Counter
from interface.observer import Observer, Subject
from business_classes.Product import Product  # Data Transfer Object


class ProductCard(ft.Card, ):
    
    def __init__(self, product: Product, on_delete = None):
        super().__init__()
        self._product = product

        self._quantity_counter_control: Counter = Counter(on_click=self._handler_on_quantity_change)
        self._cost_text_field_control: ft.TextField = ft.TextField(value=f'{product.cost_price:,.2f}', on_change=self._handler_on_cost_change)
        self._total_cost_text_control: ft.Text = ft.Text(f'Total: ${self._total_cost:,.2f} MXN')

        self.content = ft.ListTile(
            leading=ft.Icon(ft.icons.SHOPPING_CART),
            title=ft.Text(product.name, size=13),
            subtitle=ft.Column(
                [
                    ft.Row(
                        [ft.Text(f'Cantidad:',), self._quantity_counter_control],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Row(
                        [ft.Text(f'Costo: $'), self._cost_text_field_control, ft.Text(' MXN')],
                        alignment=ft.MainAxisAlignment.START,
                    )
                ],
            ),
            trailing=ft.IconButton(ft.icons.DELETE, on_click=on_delete, data=product),
        )
    
    @property
    def _quantity(self) -> int:
        return int(self._quantity_counter_control.value or 0)
    
    @property
    def _cost(self) -> float:
        return float(self._cost_text_field_control.value or 0)
    
    @property
    def _total_cost(self) -> float:
        return float(self._quantity_counter_control.value or 0) * float(self._cost_text_field_control.value or 0)
    
    def _update_product_data(self):
        self._product.cost_price = self._cost
        self._product.quantity = self._quantity
        self.data = self._product
    
    def _update_total_cost_control(self):
        self._total_cost_text_control.value = f'Total: ${self._total_cost:,.2f} MXN'
        self._total_cost_text_control.update()
        self._update_product_data()
    
    # Eventos

    def _handler_on_quantity_change(self, event: ft.ControlEvent):
        self._update_total_cost_control()
    
    def _handler_on_cost_change(self, event: ft.ControlEvent):
        self._update_total_cost_control()



class ProductSet(set[Product]):
    def __init__(self):
        super().__init__()

    def add_product(self, product: Product):
        self.add(product)
    
    def remove_item(self, product: Product):
        self.remove(product)
    
    def clear_items(self):
        self.clear()


class WidgetItemList(ft.Card):
    def __init__(self, title: str):
        super().__init__(elevation=10, expand=True, width=400)

        self._title = ft.Row([ft.Text(title, size=21)], alignment=ft.MainAxisAlignment.CENTER)
        self._date = ft.Row([ft.Text(f'{dt.now().date()}')], alignment=ft.MainAxisAlignment.CENTER)
        self.top_controls = [self._title, self._date, ft.Divider()]

        self._total_purchase_text = TotalPurchaseText() # Aquí se debe mostrar la actualización del total con el observer
        self._action_buttons = ft.Row(
            [
                ft.ElevatedButton('Limpiar', expand=True, on_click=self.handle_on_clear_widgets),
                ft.ElevatedButton('Procesar', expand=True)
            ], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        self.bottom_controls = [self._total_purchase_text, self._action_buttons]

        self.item_set = ProductSet()
        self.middle_controls = [self._build_middle_controls()]
        self.content = self._build_content()

    def add_product(self, product: Product):
        self._update_product_set_with(self.item_set.add_product, product)

    def handle_on_clear_widgets(self, event: ft.ControlEvent):
        self._clear_widget_items()
    
    def handle_on_delete_product(self, event: ft.ControlEvent):
        product = event.control.data
        self._remove_product(product)

    def _remove_product(self, product: Product):
        self._update_product_set_with(self.item_set.remove_item, product)

    def _clear_widget_items(self):
        self._update_product_set_with(self.item_set.clear_items)

    def _update_product_set_with(self, operation, product=None):
        if product:
            operation(product)
        else:
            operation()
        self._update_controls_and_content()

    def _update_controls_and_content(self):
        self.middle_controls = [self._build_middle_controls()]
        self.content = self._build_content()
        self.update()
    
    def _build_widgets(self):
        return [
            ProductCard(product=product, on_delete=self.handle_on_delete_product, total_purchase_text=self._total_purchase_text)
            for product in self.item_set
        ]
    
    def _build_middle_controls(self):
        return ft.ListView(
            controls=[
                *self._build_widgets()
            ],
            expand=True
        )
    
    def _build_content(self):
        return ft.Container(
            content=ft.Column(
                [
                    *self.top_controls,
                    *self.middle_controls,
                    *self.bottom_controls
                ],
            ),
            padding=20,
        )
    