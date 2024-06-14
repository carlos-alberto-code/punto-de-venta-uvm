import flet as ft
from interface.observer import Observer, Subject
from business_classes.Product import Product as Product # Data Transfer Object
from components.counters import Counter


class TotalProductText(ft.Text, Subject):

    def __init__(self, value: str = '0.00'):
        super().__init__()
        Subject.__init__(self)
        self.data: float = float(value)
        self.value: str = f'${self.data:,.2f} MXN'
    
    @property
    def get_data(self):
        return self.data

    @get_data.setter
    def set_data(self, value: float):
        self.data = value
        self.value = f'${self.data:,.2f} MXN'
        self.update()
    
    def subscribe_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def unsubscribe_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def inform_observers(self):
        for observer in self.observers:
            observer.synchronize(self)


class TotalPurchaseText(ft.Text, Observer):

    def __init__(self):
        super().__init__()
        self.value: str = 'Total: $0.00 MXN'
        self.subjects: list[Subject] = []
    
    def synchronize(self, subject: Subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
        self.data = sum(float(sub.data) for sub in self.subjects) # type: ignore
        self.value = f'${self.data:,.2f} MXN'
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
        self.total_product_text.set_data = float(counter_value) * float(self.product.cost_price)
        