import flet as ft
from time import sleep

from pytest import mark
from .filter_interface import IFilter


ft.Card()
class SearchResult(ft.Card):
    def __init__(self, text: str) -> None:
        super().__init__()
        # self.elevation = 3
        # self.margin = 6
        self.content = ft.Container(
            height=30,
            alignment=ft.alignment.center,
            ink=True, 
            content=ft.Text(value=text),
            on_click=lambda e: print(f'You clicked on {text}'),
        )


ft.SearchBar()
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
        self.on_change = self.update_results

    def _create_popup_menu_button(self):
        return ft.PopupMenuButton(
            icon=ft.icons.FILTER_LIST,
            menu_position=ft.PopupMenuPosition.UNDER,
            items=[self._create_popup_menu_item(key) for key in self.controllers.keys()],
        )

    def _create_popup_menu_item(self, key):
        return ft.PopupMenuItem(text=key, icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher)

    def do_nothing(self, event):
        self.close_view()
    

    def run_searcher(self, event):
        self.close_view()
        self.contoller = self.controllers[event.control.text]
        instances = self.controllers[event.control.text].get_all()
        sleep(0.1)
        new_controls = [
            SearchResult(
            text=instance.name,
            ) for instance in instances
        ]
        self.controls = [
            *new_controls,
            ft.ElevatedButton(text='Nueva', icon=ft.icons.ADD)
        ]
        self.open_view()
    
    def update_results(self, event):
        self.close_view(event.data)
        results = self.contoller.search(event.data)
        sleep(0.01)
        new_controls = [
            SearchResult(
                text=result.name
            ) for result in results
        ]
        self.controls = [
            *new_controls,
            ft.ElevatedButton(text='Nueva', icon=ft.icons.ADD)
        ]
        self.open_view()
        