import flet as ft


_table = ft.DataTable(
    sort_column_index=0,
    sort_ascending=False,
    columns=[
        ft.DataColumn(ft.Text('CODIGO'),numeric=True, on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
        ft.DataColumn(ft.Text('NOMBRE DEL PRODUCTO')),
        ft.DataColumn(ft.Text('CANTIDAD')),
        ft.DataColumn(ft.Text('COSTO UNITARIO')),
        ft.DataColumn(ft.Text('PRECIO FINAL')),
    ],
    rows=[
        # Add rows with client data here
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('5')),
                ft.DataCell(ft.Text('producto 1')),
                ft.DataCell(ft.Text('50')),
                ft.DataCell(ft.Text("$$", semantics_label="Double dollars")),
                ft.DataCell(ft.Text('560'))
            ]
        ),
    ]
)

InventorySection = ft.Column(
    controls=[
        ft.Row(
            [
                ft.Icon(name=ft.icons.INVENTORY),
                ft.Text('Inventario',size=25),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                _table
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    ]
) 