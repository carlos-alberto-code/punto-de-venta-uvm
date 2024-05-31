import flet as ft

from page.components.counters import Counter
from page.modules.content.inventory.searchers import SimpleModelSearcher as Searcher
from controllers.controllers import UnitController, CategoryController, BrandController


ft.AlertDialog()
class ProductForm(ft.AlertDialog):

    def __init__(self):
        super().__init__()
        self.title = ft.Text('Nuevo producto')
        self.icon = ft.Icon(str(ft.icons.INVENTORY))
        self.scrollable = True
        self.content = ft.Column(
            controls=[
                # ft.Row(
                #     [
                #         ft.Container(
                #             height=100,
                #             width=100,
                #             margin=10,
                #             border=ft.border.all(0.5),
                #             border_radius=10,
                #             ink=True,
                #             alignment=ft.alignment.center,
                #             content=ft.Icon(str(ft.icons.IMAGE), size=50),
                #             on_click=lambda _: print('Subir imagen'),
                #         )
                #     ],
                #     alignment=ft.MainAxisAlignment.CENTER
                # ),
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
            ft.ElevatedButton(text='Guardar', on_click=lambda _: print('Guardar')),
        ]
