import flet as ft

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
                ft.DataCell(ft.Text('1')),
                ft.DataCell(ft.Text('Coca-Cola')),
                ft.DataCell(ft.Text('5591616910')),
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('2')),
                ft.DataCell(ft.Text('Mazda')),
                ft.DataCell(ft.Text('5591616910')),
            ]
        ),
    ]
)

ProvidersSection = ft.Column(
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