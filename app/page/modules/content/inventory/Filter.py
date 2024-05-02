'''
Filter es un componente diseñado para filtrar y buscar valores de propiedades
de alguna entidad de base de datos. En el primer caso de uso se usa para filtrar
y buscar productos en función de sus unidades, categorías y marcas.
'''

from time import sleep
import flet as ft


class FilterButton(ft.PopupMenuButton):
    def __init__(self, props: str, e) -> None:
        super().__init__(
            items=[
                ft.PopupMenuItem(
                    text=name,
                    icon=ft.icons.ARROW_DROP_DOWN_CIRCLE,
                    on_click=e
                ) for name in props
            ],
            icon=ft.icons.FILTER_LIST,
            icon_size=18,
        )


class Filter(ft.SearchBar):
    def __init__(self, properties: str) -> None:
        super().__init__()
        self._filters = properties
        self.width = 400
        self.height = 40
        self.bar_leading = ft.Icon(name=ft.icons.SEARCH_SHARP, size=18)
        self.view_leading = ft.Icon(name=ft.icons.SEARCH_SHARP, size=18)
        self.bar_hint_text = 'Selecciona un filtro'
        self.view_hint_text_style = ft.TextStyle(size=18)
        self.bar_trailing = [FilterButton(properties)]
        self.view_trailing = [
            FilterButton(properties),
            ft.IconButton(
                icon=ft.icons.CLOSE,
                on_click=lambda _: self.close_view(),
                icon_size=18
            )
        ]
        self.on_tap = self.do_nothing
    
    def do_nothing(self, e):
        pass