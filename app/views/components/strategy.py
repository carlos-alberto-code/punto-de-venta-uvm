import flet as ft

class CounterStrategy:

    def increment(self, value: str) -> str:
        """Incrementa el valor."""
        raise NotImplementedError

    def decrement(self, value: str) -> str:
        """Decrementa el valor."""
        raise NotImplementedError


class IntCounterStrategy(CounterStrategy):

    def increment(self, value: str) -> str:
        return str(int(value) + 1)

    def decrement(self, value: str) -> str:
        return str(int(value) - 1)


class FloatCounterStrategy(CounterStrategy):

    def increment(self, value: str) -> str:
        return str(float(value) + 1.0)

    def decrement(self, value: str) -> str:
        return str(float(value) - 1.0)


class Counter(ft.UserControl):

    def __init__(self, strategy: CounterStrategy, allow_decimal: bool = False) -> None:
        super().__init__()
        self.strategy = strategy
        regex_pattern = r"^[0-9]*$" if not allow_decimal else r"^[0-9]*\.?[0-9]+$"
        self.field = ft.TextField(
            value='0',
            input_filter=ft.InputFilter(allow=True, regex_string=regex_pattern)
        )
        self.add_button = ft.IconButton(icon=ft.icons.ADD, on_click=self._increment)
        self.remove_button = ft.IconButton(icon=ft.icons.REMOVE, on_click=self._decrement)

    def _increment(self, event):
        self.field.value = self.strategy.increment(self.field.value) # type: ignore
        self.update()

    def _decrement(self, event):
        self.field.value = self.strategy.decrement(self.field.value) # type: ignore
        self.update()

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                self.remove_button,
                self.field,
                self.add_button,
            ],
        )
