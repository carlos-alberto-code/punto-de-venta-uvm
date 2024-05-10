import flet as ft
from time import sleep
from .filter_interface import IFilter

class SearchBarFilter(ft.SearchBar):
    def __init__(
            self,
            width: int = 400,
            height: int = 40,
            tooltip: str = 'Selecciona un filtro y escribe el nombre de la unidad, categoría o marca que deseas buscar',
            **controllers: IFilter
    ) -> None:
        super().__init__()
        self.controllers = controllers
        self.width = width
        self.height = height
        self.tooltip = tooltip
        self.bar_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.view_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.bar_hint_text = 'Selecciona un filtro'
        self.bar_trailing = [self._create_popup_menu_button()]
        self.view_trailing = [self._create_popup_menu_button(), ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view())]
        self.on_tap = self.do_nothing
        self.controls = [ft.ElevatedButton(text='Agregar nueva propiedad', icon=ft.icons.ADD)]

    def _create_popup_menu_button(self):
        return ft.PopupMenuButton(
            icon=ft.icons.FILTER_LIST,
            menu_position=ft.PopupMenuPosition.UNDER,
            items=[self._create_popup_menu_item(key) for key in self.controllers.keys()]
        )

    def _create_popup_menu_item(self, key):
        return ft.PopupMenuItem(text=key, icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher)

    def do_nothing(self, event):
        self.close_view()

    def run_searcher(self, event):
        self.view_hint_text = f'Escribe el nombre de la {event.control.text.lower()}'
        self.close_view()
        sleep(0.08)
        self.open_view()