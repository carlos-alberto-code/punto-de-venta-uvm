from time import sleep
from typing import Any, Optional

import flet as ft

from interfaces.interfaces import ControllerInterface as Controller
from page.modules.content.inventory.ProductTable import ProductTable


class SearchResult(ft.Card):
    '''
    Represents a search result in the search bar.
    The id is the id of the record in the database, and the text is the name of the record.
    It stores the id and the name in the data attribute of the control for later use.
    '''
    def __init__(
            self,
            id:int,
            text: str,
            on_click=None
    ) -> None:
        super().__init__()
        self.content = ft.Container(
            height=30,
            padding=ft.Padding(left=10, right=0, top=0, bottom=0),
            alignment=ft.alignment.center,
            border_radius=10,
            ink=True,
            data={'id': id, 'name': text},
            content=ft.Row(
                controls=[
                    ft.Icon(str(ft.icons.HISTORY), size=15),
                    ft.Text(value=text),
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            on_click=on_click,
        )
        

class SimpleModelSearcher(ft.SearchBar):

    def __init__(
            self,
            model_controller: Controller,
    ):
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
            # on_change=self.hand,
            on_tap=self.handler_on_tap,
            # on_submit=on_submit,
        )
        self.controller = model_controller
        self.controls = [
            *self.create_search_results(self.controller.get_all()),
            ft.ElevatedButton(
                text='Nuevo',
                on_click=self._handle_on_click_new,
            ),
        ]
    
    # Evento del botón 'Nuevo'
    def _handle_on_click_new(self, event): #TODO: A la espera de refactorizar esta característica
        event.page.bottom_sheet = ft.BottomSheet()
        event.page.bottom_sheet.open = True
        event.page.update()
        print('Se oprimió el botón nuevo')
    
    def create_search_results(self, intances: list) -> list[ft.Control]: # Función útil dentro y fuera del contexto
        return [
            SearchResult(id=instance.id, text=instance.name, on_click=self.handle_on_click_result)
            for instance in intances
        ]
    
    def handle_on_click_result(self, event): # Funcióna para manejar los resultados internos
        self.data = event.control.data # Referencía al diccionario del control en donde se hizo click
        self.close_view(event.control.data['name'])

    def handler_on_tap(self, event: ft.ControlEvent):
        self.data = ''
        self.value = ''
        self.update()
        sleep(1)
    
    # def handler_on_change(self, event: ft.ControlEvent):
    #     self.update()


class ProductSearcher(ft.SearchBar):

    def __init__(self, product_controller: Controller,  product_table: ProductTable) -> None:
        super().__init__(
            width=300,
            height=40,
            bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
            bar_hint_text='Buscar producto',
            tooltip='Clic para restaruar la tabla de productos',
            on_tap=self.handler_on_tap,
            on_change=self.handler_on_change,
        )
        self.controller = product_controller
        self.table = product_table
    
    def handler_on_tap(self, event: ft.ControlEvent):
        self.close_view()
        self.table.products = self.controller.get_all()
    
    def handler_on_change(self, event: ft.ControlEvent):
        val = str(self.value)
        self.table.products = self.controller.search(val)
    

    