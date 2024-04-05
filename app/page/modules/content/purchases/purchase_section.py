import flet as ft

_title = ft.Text('Compras')
_add_button = ft.ElevatedButton("Agregar cliente", icon="Check_circle")
_edit_button = ft.ElevatedButton("Editar cliente", icon="Edit")
_delete_button = ft.ElevatedButton("Eliminar cliente", icon="Delete")
_table = ft.DataTable(
    sort_column_index=0,
    sort_ascending=False,
    columns=[
        ft.DataColumn(ft.Text('ID'), numeric=True, on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
        ft.DataColumn(ft.Text('PROVEEDOR ID')),
        ft.DataColumn(ft.Text('FECHA')),
        ft.DataColumn(ft.Text('TOTAL')),
    ],
    rows=[
        # Add rows with client data here
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('5')),
                ft.DataCell(ft.Text('12321')),
                ft.DataCell(ft.Text('')),
                ft.DataCell(ft.Text('2045')),
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('2')),
                ft.DataCell(ft.Text('235463653')),
                ft.DataCell(ft.Text('')),
                ft.DataCell(ft.Text('8756')),
            ]
        )
    ]
)

PurchaseSection = ft.Column(
    controls=[
        ft.Row(
            [_title],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [_add_button,_edit_button,_delete_button],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [_table],
            alignment= ft.MainAxisAlignment.CENTER
        )
    ]
) 