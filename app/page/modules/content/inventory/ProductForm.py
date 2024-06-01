import flet as ft

from page.components.counters import Counter
from page.modules.content.inventory.searchers import SimpleModelSearcher as Searcher
from controllers.controllers import UnitController, CategoryController, BrandController


ft.AlertDialog()
class ProductForm(ft.AlertDialog):

    def __init__(self, on_save_click=None):
        super().__init__(
            title=ft.Text('Nuevo producto'),
            icon=ft.Icon(str(ft.icons.INVENTORY)),
            scrollable=True,
        )
        self.content = ft.Column(
            controls=[
                Searcher(UnitController()),
                Searcher(CategoryController()),
                Searcher(BrandController()),
                ft.Row(
                    [
                        ft.Text('Cantidad:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Text('Precio de compra:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Text('Precio de venta:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Text('Existencias mínimas:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ],
        )
        self.actions = [
            ft.ElevatedButton(text='Limpiar', on_click=lambda _: print('Limpiar')),
            ft.ElevatedButton(text='Guardar', on_click=on_save_click),
        ]
