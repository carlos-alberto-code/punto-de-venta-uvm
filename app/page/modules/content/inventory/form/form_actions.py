# Son los botones de acción del formulario de productos
from flet import ElevatedButton


class CancelButton(ElevatedButton):
    def __init__(self, on_click=None):
        super().__init__(
            text='Cancelar',
            on_click=on_click,
        )

class CleanButton(ElevatedButton):
    def __init__(self, on_click=None):
        super().__init__(
            text='Limpiar',
            on_click=on_click,
        )

class SaveButton(ElevatedButton):
    def __init__(self, on_click=None):
        super().__init__(
            text='Guardar',
            on_click=on_click,
        )