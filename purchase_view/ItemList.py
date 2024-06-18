from decimal import Decimal
import flet as ft
from datetime import datetime as dt
from business_classes.Product import Product  # Data Transfer Object
from purchase_view.ProductFormCard import ProductFormCard

from components.searchers import SimpleModelSearcher
from controllers.controllers import SuplierController
from controllers.controllers import PurchaseDetailController


class PurchaseList(ft.Card):
    def __init__(self, title: str):
        super().__init__(elevation=10, expand=True, width=400)

        self._title = ft.Row([ft.Text(title, size=21)], alignment=ft.MainAxisAlignment.CENTER)
        self.date = dt.now().date()
        self._date_row = ft.Row([ft.Text(f'{self.date}')], alignment=ft.MainAxisAlignment.CENTER)
        
        self.top_controls = [self._title, self._date_row, ft.Divider()]

        self._action_buttons = ft.Row(
            [
                ft.ElevatedButton('Limpiar', expand=True, on_click=self.handle_on_clear_widgets),
                ft.ElevatedButton('Guardar', expand=True, on_click=self.handle_on_save)
            ], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        self.bottom_controls = [self._action_buttons]

        self.product_set: set[Product] = set()
        self.middle_controls = [self._create_product_list_view()]
        self.content = self._create_content()

    # Public methods ----------------------------------------------------------

    def add_product(self, product: Product):
        self._update_product_set_and_controls(self.product_set.add, product)

    # Event handlers ----------------------------------------------------------

    def handle_on_clear_widgets(self, event: ft.ControlEvent):
        self._clear_product_cards()
    
    def handle_on_delete_product(self, event: ft.ControlEvent):
        product = event.control.data
        self._remove_product(product)

    def handle_on_save(self, event: ft.ControlEvent):
        if self._supplier_searcher.data:
            purchase_detail_controller = PurchaseDetailController()
            purchase_detail = [
                {
                    'product_id': product.product_id,
                    'quantity': product.quantity,
                    'unit_purchase_price': product.cost_price,
                    'total_unit_price': product.total_cost,

                } for product in self.product_set
            ]
            purchase = {
                'supplier_id': self._supplier_searcher.data['id'],
                'date': self.date,
                'total': sum([product.total_cost for product in self.product_set]),
            }
            purchase_detail_controller.create_with_details(purchase_detail, **purchase)

    # Private methods ---------------------------------------------------------

    def _remove_product(self, product: Product):
        self._update_product_set_and_controls(self.product_set.remove, product)

    def _clear_product_cards(self):
        self._update_product_set_and_controls(self.product_set.clear)

    def _update_product_set_and_controls(self, operation, product=None):
        if product:
            operation(product)
        else:
            operation()
        self._update_controls_and_content()

    def _update_controls_and_content(self):
        self.middle_controls = [self._create_product_list_view()]
        self.content = self._create_content()
        self.update()
    
    # Creation methods --------------------------------------------------------

    def _create_product_widgets(self):
        return [
            ProductFormCard(product=product, on_delete=self.handle_on_delete_product)
            for product in self.product_set
        ]
    
    def _create_product_list_view(self):
        return ft.ListView(
            controls=[
                *self._create_product_widgets()
            ],
            expand=True
        )
    
    def _create_content(self):
        self._supplier_searcher = SimpleModelSearcher(SuplierController())
        return ft.Container(
            content=ft.Column(
                [
                    *self.top_controls,
                    self._supplier_searcher,
                    *self.middle_controls,
                    *self.bottom_controls
                ],
            ),
            padding=20,
        )
    