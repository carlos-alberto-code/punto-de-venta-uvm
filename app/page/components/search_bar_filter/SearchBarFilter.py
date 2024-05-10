'''
Filter es un componente diseñado para filtrar y buscar valores de propiedades
de alguna entidad de base de datos. En el primer caso de uso se usa para filtrar
y buscar productos en función de sus unidades, categorías y marcas.
'''

from time import sleep
import flet as ft

from page.components.search_bar_filter.filter_interface import IFilter


class FilterButton(ft.PopupMenuButton):
    def __init__(self, e, **controllers: IFilter) -> None:
        super().__init__()
        self.icon = ft.icons.FILTER_LIST
        self.controllers = controllers
        self.items = [self.create_item(name) for name in self.controllers.keys()]
    
    def create_item(self, name: str, on_click=None):
        return ft.PopupMenuItem(
            text=name,
            icon=ft.icons.ARROW_DROP_DOWN_CIRCLE,
            on_click=on_click
        )


ft.SearchBar()
class SearchBarFilter(ft.SearchBar):
    # Esta clase es un componente de búsqueda y filtrado, pensado para buscar y filtrar en función de las unidades, categorías y marcas
    def __init__(self, **controllers: IFilter) -> None:
        super().__init__()
        self.controllers = controllers
        self.width = 400
        self.height = 40
        self.tooltip = 'Selecciona un filtro y escribe el nombre de la unidad, categoría o marca que deseas buscar'
        self.bar_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.view_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.bar_hint_text = 'Selecciona un filtro'
        self.bar_trailing = [
            ft.PopupMenuButton(
            icon=ft.icons.FILTER_LIST,
            items=[
                ft.PopupMenuItem(text=key, icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher)
                for key in self.controllers.keys()
            ]
            )
        ]
        self.view_trailing = [
            ft.PopupMenuButton(
            icon=ft.icons.FILTER_LIST,
            items=[
                ft.PopupMenuItem(text=key, icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher)
                for key in self.controllers.keys()
            ]
            ),
            ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view()),
        ]
        self.on_tap = self.do_nothing
        self.controls = [ft.ElevatedButton(text='Agregar nueva propiedad', icon=ft.icons.ADD)]
    
    def do_nothing(self, event):
        self.close_view()
    
    def run_searcher(self, event):
        self.view_hint_text = f'Escribe el nombre de la {event.control.text.lower()}'
        self.close_view()
        sleep(0.08)
        self.open_view()
        # Colocar los controles de búsqueda en función del filtro seleccionado
        
