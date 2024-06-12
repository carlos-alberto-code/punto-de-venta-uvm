import flet as ft
from typing import Optional
from controllers.ControllerInterface import ControllerInterface as Controller


class Searcher(ft.SearchBar):
    
    def __init__(self,  controller: Optional[Controller] = None, on_change=None):
        super().__init__(
            height=40,
            bar_hint_text='Proveedor',
            bar_leading=ft.Icon(ft.icons.SEARCH, size=18),
            view_leading=ft.Icon(ft.icons.SEARCH, size=18),
            bar_trailing=[ft.Icon(ft.icons.ARROW_DROP_DOWN)],
            view_trailing=[ft.IconButton(ft.icons.CLOSE, icon_size=18, on_click=lambda e: self.close_view())],
            on_change=on_change,
        )
        if controller:
            self.controller = controller
        else:
            self.bar_hint_text = 'No hay controlador'