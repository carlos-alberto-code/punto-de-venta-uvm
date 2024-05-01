import flet as ft
import sys
sys.path.append('..')
from controllers.categories_controller import CategorieController

_search_bar = ft.TextField(
    label='Buscar',
)

class CategorySection(ft.Column):

    def __init__(self):
        super().__init__()
        self.categories = CategorieController().get_all()
        self.sort_functions = {
            'id': lambda: self.sort_by('id', int),
            'name': lambda: self.sort_by('name', lambda x: str(x).lower())
        }
        self.sort_order = {key: True for key in self.sort_functions.keys()}
        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    _search_bar
                ]
            ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.TextButton('ID',on_click=lambda event: self.sort_by_key('id', event))),
                    ft.DataColumn(ft.TextButton('NOMBRE',on_click=lambda event: self.sort_by_key('name', event))),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(category.id))),
                            ft.DataCell(ft.Text(str(category.name))),
                        ],
                        selected=True,
                        on_select_changed=lambda event: print(event),
                    )for category in self.categories
                ]

            )
        ]

    def sort_by(self, attribute, type):
        reverse_order = not self.sort_order[attribute]
        self.categories = sorted(self.categories, key=lambda category: type(getattr(category, attribute)), reverse=reverse_order)
        self.sort_order[attribute] = reverse_order
        self.update_table()
    def update_table(self):
        self.controls[1].rows = [ # type: ignore
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(category.id))),
                    ft.DataCell(ft.Text(str(category.name))),
                ],
                selected=True,
                on_select_changed=lambda e: print(type(e)),
            ) for category in self.categories
        ]
    
    def sort_by_key(self, key: str, event: ft.ControlEvent):
        self.sort_functions[key]()
        self.update()


_title = ft.Text('Categorias',size=25)
_table = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('NOMBRE'))
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(categorie.id))),
                ft.DataCell(ft.Text(categorie.name))
            ]
        )for categorie in CategorieController().get_all()
    ]
)

CategoriesSection = ft.Column(
    scroll=ft.ScrollMode.ALWAYS,
    controls=[
        ft.Row(
            [
                ft.Icon(name=ft.icons.CHECKLIST_ROUNDED),
                _title
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [_table],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ]
)