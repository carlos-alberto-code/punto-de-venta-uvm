import flet as ft
from controllers.supplier_controller import SupplierController

_search_bar = ft.TextField(
    label='Buscar',
)

class SupplierSection(ft.Column):

    def __init__(self):
        super().__init__()
        self.suppliers = SupplierController().get_all()
        self.sort_functions = {
            'id': lambda: self.sort_by('id', int),
            'name': lambda: self.sort_by('name', lambda x: str(x).lower()),
            'phone': lambda: self.sort_by('phone', lambda x: str(x).lower())
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
                    ft.DataColumn(ft.TextButton('ID', on_click=lambda event: self.sort_by_key('id', event))),
                    ft.DataColumn(ft.TextButton('NOMBRE', on_click=lambda event: self.sort_by_key('name', event))),
                    ft.DataColumn(ft.TextButton('TELEFONO', on_click=lambda event: self.sort_by_key('phone', event)))
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(supplier.id))),
                            ft.DataCell(ft.Text(str(supplier.name))),
                            ft.DataCell(ft.Text(str(supplier.phone))),
                        ],
                        selected=True,
                    ) for supplier in self.suppliers
                ]
            )
        ]

    def sort_by(self, attribute, type):
        reverse_order = not self.sort_order[attribute]
        self.suppliers = sorted(self.suppliers, key=lambda supplier: type(getattr(supplier, attribute)), reverse=reverse_order)
        self.sort_order[attribute] = reverse_order
        self.update_table()

    def update_table(self):
        self.controls[1].rows = [ # type: ignore
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(supplier.id))),
                    ft.DataCell(ft.Text(str(supplier.name))),
                    ft.DataCell(ft.Text(str(supplier.phone))),
                ],
                selected=True,
                on_select_changed=lambda e: print(type(e)),
            ) for supplier in self.suppliers
        ]
    
    def sort_by_key(self, key: str, event: ft.ControlEvent):
        self.sort_functions[key]()
        self.update()

_title = ft.Text('Proveedores', size=25)
_table = ft.DataTable(
    sort_column_index=0,
    sort_ascending=False,
    columns=[
        ft.DataColumn(ft.Text('ID'),numeric=True, on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
        ft.DataColumn(ft.Text('PROVEEDOR')),
        ft.DataColumn(ft.Text('TELEFONO'), numeric=True),
                
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(supplier.id))),
                ft.DataCell(ft.Text(supplier.name)),
                ft.DataCell(ft.Text(supplier.phone)),
            ]
        )for supplier in SupplierController().get_all()
    ]
)

ProvidersSection = ft.Column(
    scroll= ft.ScrollMode.ALWAYS,
    controls=[
        ft.Row(
            [
                ft.Icon(name=ft.icons.PERSON_PIN_ROUNDED),
                _title
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [_table],
            alignment=ft.MainAxisAlignment.CENTER
        )
    ]
)