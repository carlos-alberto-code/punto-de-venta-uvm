# TODO: Evitar la escritura de texto pero permitir puntos decimales.
# TODO: En los valores flotantes solo debe permitir dos digitos
import flet as ft


class _CounterStrategy:
    def increment(self, value: str) -> str:
        return str()

    def decrement(self, value: str) -> str:
        return str()


class IntCounter(_CounterStrategy):
    def increment(self, value: str) -> str:
        return str(int(value) + 1)

    def decrement(self, value: str) -> str:
        return str(int(value) - 1)


class FloatCounter(_CounterStrategy):
    def increment(self, value: str) -> str:
        return str(float(value) + 1.0)

    def decrement(self, value: str) -> str:
        return str(float(value) - 1.0)


class Counter(ft.UserControl):
    def __init__(
            self,
            strategy: _CounterStrategy,
            start_value: int = 0,
            end_value: int = 1_000_000,
            title_msg: str = 'No title',
            msg: str = 'No message'
    ):
        super().__init__()
        self._strategy = strategy
        self._start = start_value
        self._end = end_value
        self._msg_title = title_msg
        self._msg = msg
        self._remove_button = ft.IconButton(icon=ft.icons.REMOVE, on_click=self._decrement)
        self._quantity_field = ft.TextField(
            border=ft.InputBorder.NONE,
            width=50,
            value=str(start_value),
            text_align=ft.TextAlign.CENTER,
            text_vertical_align=ft.VerticalAlignment.START,
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self._add_button = ft.IconButton(icon=ft.icons.ADD, on_click=self._increment)

    @property
    def value(self):
        return (
            int(str(self._quantity_field.value))
            if isinstance(self._strategy, IntCounter)
            else float(str(self._quantity_field.value))
        )

    def _increment(self, e):
        self._quantity_field.value = self._strategy.increment(str(self._quantity_field.value)) if int(str(self._quantity_field.value)) < self._end else str(self._end)
        e.page.update()

    def _decrement(self, e):
        self._quantity_field.value = self._strategy.decrement(str(self._quantity_field.value)) if int(str(self._quantity_field.value)) > self._start else str(self._start)
        e.page.dialog = Alert(
            title=self._msg_title,
            msg=self._msg
        ).build()
        e.page.update()

    def build(self):
        return ft.Row(
            controls=[
                self._remove_button,
                self._quantity_field,
                self._add_button
            ]
        )


class Alert(ft.UserControl):
    
    def __init__(self, title: str, msg: str):
        super().__init__()
        self.title = title
        self.msg = msg
        self.alert = ft.AlertDialog(
            open=True,
            title=ft.Text(value=self.title),
            content=ft.Text(value=self.msg)
        )

    def build(self):
        return self.alert
