'''
Filter es un componente diseñado para filtrar y buscar valores de propiedades
de alguna entidad de base de datos. En el primer caso de uso se usa para filtrar
y buscar productos en función de sus unidades, categorías y marcas.
'''

from time import sleep
import flet as ft

from controllers.filter_interface import IFilter


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


ft.SearchBar()
class SearchBarFilter(ft.SearchBar):
    
    def __init__(self, **controllers: IFilter) -> None:
        super().__init__()
        self.controllers = controllers
        print(self.controllers.keys())
        print(self.controllers['Marca'].get_all_values())
        
        
        self.width = 400
        self.height = 40
        self.bar_leading = ft.Icon(name=ft.icons.SEARCH_SHARP, size=18)
        self.view_leading = ft.Icon(name=ft.icons.SEARCH_SHARP, size=18)
        self.bar_hint_text = 'Selecciona un filtro'
        self.view_hint_text_style = ft.TextStyle(size=18)
        # self.bar_trailing = [FilterButton(properties)]
        # self.view_trailing = [
        #     FilterButton(properties),
        #     ft.IconButton(
        #         icon=ft.icons.CLOSE,
        #         on_click=lambda _: self.close_view(),
        #         icon_size=18
        #     )
        # ]
        self.on_tap = self.do_nothing
    
    def do_nothing(self, event):
        self.close_view()



#### 



class Filter(ft.SearchBar):
    # Esta clase es un componente de búsqueda y filtrado, pensado para buscar y filtrar en función de las unidades, categorías y marcas
    def __init__(self):
        super().__init__()
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
                    ft.PopupMenuItem(text='Unidad', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Categoría', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Marca', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                ]
            )
        ]
        self.view_trailing = [
            ft.PopupMenuButton(
                icon=ft.icons.FILTER_LIST,
                items=[
                    ft.PopupMenuItem(text='Unidad', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Categoría', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Marca', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                ]
            ),
            ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view()),
        ]
        self.on_tap = self.do_nothing
        # Siempre debe ir un control al final que permita agregar una nueva propiedad, dependiendo del filtro seleccionado
        # Al seleccionarse un filtro, se inyectan los controles dependiendo la opción seleccionada.
        # Pero siempre estará el control para registrar una nueva propiedad al final de las opciones.
        self.controls = [ft.ElevatedButton(text='Agregar nueva propiedad', icon=ft.icons.ADD)]
    
    def do_nothing(self, event):
        self.close_view()
    
    def run_searcher(self, event):
        self.view_hint_text = f'Escribe el nombre de la {event.control.text.lower()}'
        self.close_view()
        sleep(0.08)
        self.open_view()
