from typing import Any, Optional
import flet as ft
from time import sleep

from interfaces.interfaces import ControllerInterface as Controller
from page.modules.content.inventory.ProductTable import ProductTable


class SearchResult(ft.Card):
    def __init__(
            self,
            id:int,
            text: str,
            on_click=None
    ) -> None:
        super().__init__(
            show_border_on_foreground=True,
        )
        self.content = ft.Container(
            height=30,
            padding=ft.Padding(left=10, right=0, top=0, bottom=0),
            alignment=ft.alignment.center,
            border_radius=10,
            ink=True,
            data={'id': id, 'name': text},
            content=ft.Row(
                controls=[
                    ft.Icon(str(ft.icons.HISTORY), size=20),
                    ft.Text(value=text),
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            on_click=on_click if on_click else lambda e: print(e.control.data)
        )
        

class SimpleModelSearcher(ft.SearchBar):

    def __init__(self, model_controller: Controller):
        super().__init__(
            width=300,
            height=40,
            bar_hint_text='Selecciona una opción',
            bar_leading=ft.Icon(name=ft.icons.SEARCH, size=20),
            view_leading=ft.Icon(name=ft.icons.SEARCH, size=20),
            bar_trailing=[ft.Icon(name=ft.icons.ARROW_DROP_DOWN_ROUNDED),],
            view_trailing=[
                ft.Icon(name=ft.icons.ARROW_DROP_DOWN_ROUNDED),
            ],
            on_change=self.handle_change_event,
            on_tap=self.handle_tap_event,
        )
        self.controls = self._create_search_results(model_controller.get_all())
        self.controls.append(ft.ElevatedButton('Nuevo'))
        self.model_controler = model_controller
    
    def _create_search_results(self, intances: list) -> list[ft.Control]:
        return [
            SearchResult(id=instance.id, text=instance.name, on_click=self.handle_on_click_result)
            for instance in intances
        ]
    
    def handle_on_click_result(self, event):
        self.data = event.control.data # Referencía a la tupla del control en donde se hizo click
        self.close_view(event.control.data['name'])

    def handle_change_event(self, event):
        self.close_view(str(self.value))
        sleep(0.01)
        results = self.model_controler.search(str(self.value))
        self.controls = self._create_search_results(results)
        self.open_view()
    
    def handle_tap_event(self, event):
        self.close_view('')
        self.open_view()
        self.update()


class ProductSearcher(ft.SearchBar):

    def __init__(self, on_change: Optional[Any] = None, on_tap: Optional[Any] = None):
        super().__init__(
            width=300,
            height=40,
            bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
            bar_hint_text='Buscar producto',
            tooltip='Clic para restaruar la tabla de productos',
            on_tap=on_tap,
            on_change=on_change,
        )
    