import flet as ft

_table = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text('CODIGO'),numeric=True, on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
        ft.DataColumn(ft.Text('NOMBRE DEL PRODUCTO')),
        ft.DataColumn(ft.Text('CANTIDAD')),
        ft.DataColumn(ft.Text('COSTO UNITARIO')),
        ft.DataColumn(ft.Text('TOTAL')),
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('5')),
                ft.DataCell(ft.Text('producto 2')),
                ft.DataCell(ft.Text('50')),
                ft.DataCell(ft.Text("$$", semantics_label="Double dollars")),
                ft.DataCell(ft.Text('560'))
            ]
        ),
    ]
)

PurchaseSection = ft.Column(
    controls=[
        ft.Row(
            [
                ft.Icon(name=ft.icons.LIBRARY_ADD_CHECK_ROUNDED),
                ft.Text('Entradas (Compras)',size=25)
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [_table],
            alignment= ft.MainAxisAlignment.CENTER
        )
    ]
)