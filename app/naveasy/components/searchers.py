import flet as ft

from interfaces.interfaces import ControllerInterface as Controller


class SimpleModelSearcher(ft.SearchBar):

    def __init__(self, model_controller: Controller):
        super().__init__(
            bar_hint_text='Selecciona una opción',
            bar_leading=ft.Icon(name=ft.icons.SEARCH, size=20),
            view_leading=ft.Icon(name=ft.icons.SEARCH, size=20),
            bar_trailing=[ft.Icon(name=ft.icons.ARROW_DROP_DOWN_ROUNDED),],
            view_trailing=[
                ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view(e.data)),
            ]
        )
        self.model_controler = model_controller
