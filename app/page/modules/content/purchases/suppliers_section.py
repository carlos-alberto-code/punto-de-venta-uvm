import flet as ft
from controllers.supplier_controller import SupplierController

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