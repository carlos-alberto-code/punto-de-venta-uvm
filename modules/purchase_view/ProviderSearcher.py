import flet as ft
from typing import Optional
from controllers.ControllerInterface import ControllerInterface as Controller


class SupplierSearcher(ft.SearchBar):
    """
    Clase que representa un buscador de proveedores.

    Args:
        controller (Optional[Controller]): El controlador asociado al buscador. (Default: None)
        on_change (callable): Función que se ejecuta cuando cambia el texto del buscador.

    Attributes:
        controller (Controller): El controlador asociado al buscador.
    """

    def __init__(self, controller: Optional[Controller] = None):
        super().__init__(
            height=40,
            bar_hint_text='Proveedor',
            bar_leading=ft.Icon(ft.icons.SEARCH, size=18),
            view_leading=ft.Icon(ft.icons.SEARCH, size=18),
            bar_trailing=[ft.Icon(ft.icons.ARROW_DROP_DOWN)],
            view_trailing=[ft.IconButton(ft.icons.CLOSE, icon_size=18, on_click=lambda e: self.close_view())],
            on_change=self.handle_on_change,
        )
        if controller:
            self.controller = controller
        else:
            self.bar_hint_text = 'No hay controlador'
    
    def handle_on_tap(self, event: ft.ControlEvent):
        self.controls = [
            
        ]
        self.open_view()

    def handle_on_change(self, event: ft.ControlEvent):
        results = self.controller.search(event.control.text)