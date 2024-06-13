import flet as ft
from datetime import datetime as dt

from components.counters import Counter
from interface.observer import Observer, Subject
from purchase_view.ProductDTO import ProductDTO as Product # Data Transfer Object


class TotalProductText(ft.Text, Subject):

    def __init__(self, value: str = '0.00'):
        super().__init__()
        Subject.__init__(self)
        self.data: float = float(value)
        self.value: str = f'${self.data:,.2f} MXN'
    
    def get_data(self):
        return self.data

    def set_data(self, value: float):
        self.data = value
        self.value = f'${self.data:,.2f} MXN'
        self.update()
    
    def subscribe_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def unsubscribe_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def inform_observers(self):
        [observer.synchronize(self) for observer in self.observers]


class TotalPurchaseText(ft.Text, Observer):

    def __init__(self):
        super().__init__()
        self.value: str = 'Total: $0.00 MXN'
        self.subjects: list[Subject] = []
    
    def synchronize(self, subject: Subject):
        self.subjects.append(subject) if subject not in self.subjects else self.subjects
        self.data = sum(float(sub.data) for sub in self.subjects) # type: ignore
        self.value = f'Total: ${self.data:,.2f} MXN'
        self.update()


class WidgetItemCard(ft.Card):
    
    def __init__(self, product: Product, on_delete=None):
        self.product = product
        self.total_product_text = TotalProductText(value=str(product.cost_price))
        super().__init__(
            content=ft.ListTile(
                leading=ft.Icon(ft.icons.SHOPPING_CART),
                title=ft.Text(f'{product.name}', size=15),
                subtitle=ft.Column(
                    [
                        ft.Row(
                            [ft.Text(f'Cantidad:', size=15), Counter(on_click=self.handler_counter_click)],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [ft.Text('Costo:'), self.total_product_text],
                            alignment=ft.MainAxisAlignment.START,
                        )
                    ]
                ),
                trailing=ft.IconButton(ft.icons.DELETE, on_click=on_delete, data=product),
            ),
            elevation=0,
        )
    
    def handler_counter_click(self, event: ft.ControlEvent):
        counter_value = event.control.data
        self.total_product_text.set_data(float(counter_value) * float(self.product.cost_price))
        self.total_product_text.update()



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

        self._total_text = ft.Row(
            [ft.Text(f'Total: ${0:,.2f} MXN', size=16)],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self._action_buttons = ft.Row(
            [
                ft.ElevatedButton('Limpiar', expand=True, on_click=self.handle_on_clear_widgets),
                ft.ElevatedButton('Procesar', expand=True)
            ], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        self.bottom_controls = [self._total_text, self._action_buttons]

        self.item_set = ProductSet()
        # self.widgets: list[WidgetItemCard] = []
        self.middle_controls = [self._build_middle_controls()]
        self.content = self._build_content()

    # Metodos públicos

    def add_product(self, product: Product):
        self._update_product_set_with(self.item_set.add_product, product)

    # Eventos

    def handle_on_clear_widgets(self, event: ft.ControlEvent):
        self._clear_widget_items()
    
    def handle_on_delete_product(self, event: ft.ControlEvent):
        product = event.control.data
        self._remove_product(product)

    # Metodos privados

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
            WidgetItemCard(product=product, on_delete=self.handle_on_delete_product)
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
    