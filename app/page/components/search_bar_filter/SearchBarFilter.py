import attr
import flet as ft
from time import sleep

from controllers.products_controller import ProductController
from page.modules.content.inventory.ProductTable import ProductTable

from .filter_interface import IFilter


class SearchResult(ft.Card):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.content = ft.Container(
            height=30,
            margin=3,
            padding=ft.Padding(left=10, right=0, top=0, bottom=0),
            alignment=ft.alignment.center,
            ink=True,
            border_radius=10,
            content=ft.Row(
                [
                    ft.Icon(str(ft.icons.CIRCLE), size=10),
                    ft.Text(value=text), 
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            on_click=lambda e: print(f'You clicked on {text}'),
        )

ft.SearchBar()
class SearchBarFilter(ft.SearchBar):
    def __init__(
            self,
            table: ProductTable,
            product_controller: ProductController,
            width: int = 350,
            height: int = 35,
            tooltip: str = 'Da clic en el icono para seleccionar un filtro',
            **filter_controllers: IFilter
    ) -> None:
        super().__init__()
        self.table = table
        self.product_controller = product_controller
        self.filter_controllers = filter_controllers
        self.width = width
        self.height = height
        self.tooltip = tooltip
        self.bar_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.view_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.bar_hint_text = 'Buscador'
        self.bar_trailing = [self._create_popup_menu_button()]
        self.view_trailing = [self._create_popup_menu_button(), ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view())]
        self.on_tap = self.do_nothing
        self.on_change = self.finding_products #self.update_results

    def _create_popup_menu_button(self):
        return ft.PopupMenuButton(
            icon=ft.icons.FILTER_LIST,
            tooltip='Abrir filtros',
            menu_position=ft.PopupMenuPosition.UNDER,
            items=[self._create_popup_menu_item(key) for key in self.filter_controllers.keys()],
        )

    def _create_popup_menu_item(self, key):
        return ft.PopupMenuItem(text=key, icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher)

    def do_nothing(self, event):
        self.close_view('')
        self.table.products = self.product_controller.get_all()
        self.table.update()
    
    def run_searcher(self, event):
        self.close_view()
        self.contoller = self.filter_controllers[event.control.text]
        instances = self.filter_controllers[event.control.text].get_all()
        sleep(0.1)
        new_controls = [
            SearchResult(
            text=instance.name,
            ) for instance in instances
        ]
        self.controls = [
            *new_controls,
            ft.ElevatedButton(text='Agregar nueva', icon=ft.icons.ADD)
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
        
    def finding_products(self, event):
        if event.data == '':
            self.table.products = self.product_controller.get_all()
            self.table.update()
        results = self.product_controller.search_products(event.data)
        self.table.products = results
        self.table.update()