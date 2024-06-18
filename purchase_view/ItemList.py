import flet as ft
from datetime import datetime as dt
from business_classes.Product import Product  # Data Transfer Object
from purchase_view.ProductFormCard import ProductFormCard


class ProductSet(set[Product]):
    def __init__(self):
        super().__init__()

    def add_product(self, product: Product):
        self.add(product)
    
    def remove_item(self, product: Product):
        self.remove(product)
    
    def clear_items(self):
        self.clear()


class PurchaseList(ft.Card):
    def __init__(self, title: str):
        super().__init__(elevation=10, expand=True, width=300)

        self._title = ft.Row([ft.Text(title, size=21)], alignment=ft.MainAxisAlignment.CENTER)
        self._date = ft.Row([ft.Text(f'{dt.now().date()}')], alignment=ft.MainAxisAlignment.CENTER)
        self.top_controls = [self._title, self._date, ft.Divider()]

        self._total_purchase_text = ft.Row(
            [ft.Text('Total de compra: $0.00 MXN')],
            alignment=ft.MainAxisAlignment.CENTER
        )
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
            ProductFormCard(product=product, on_delete=self.handle_on_delete_product)
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
    