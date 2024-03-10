import flet as ft


class CounterStrategy:

    def increment(self, value: str) -> str:
        return str()

    def decrement(self, value: str) -> str:
        return str()


class IntCounter(CounterStrategy):
    
    def increment(self, value: str) -> str:
        return str(int(value) + 1)
    
    def decrement(self, value: str) -> str:
        return str(int(value) - 1)


class FloatCounter(CounterStrategy):

    def increment(self, value: str) -> str:
        return str(float(value) + 1.0)
    
    def decrement(self, value: str) -> str:
        return str(float(value) - 1.0)


class Counter(ft.UserControl):

    def __init__(self, strategy: CounterStrategy):
        super().__init__()
        self.strategy = strategy
        self.remove_button = ft.IconButton(icon=ft.icons.REMOVE, on_click=self._decrement)
        self.field = ft.TextField(
            value='0',
            text_align=ft.TextAlign.CENTER,
            text_vertical_align=ft.VerticalAlignment.START,
        )
        self.add_button = ft.IconButton(icon=ft.icons.ADD, on_click=self._increment)
    
    def _increment(self, e):
        self.field.value = self.strategy.increment(str(self.field.value))
        self.update()

    def _decrement(self, e):
        self.field.value = self.strategy.decrement(str(self.field.value))
        self.update()
    
    def build(self):
        return ft.Row(
            height=40,
            controls=[
                self.remove_button,
                self.field,
                self.add_button
            ]
        )