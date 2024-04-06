import flet as ft

# Create search bar
_search_bar = ft.TextField(hint_text="Buscar cliente", width=200, height=50, icon=ft.icons.SEARCH)

# Create buttons
_add_button = ft.ElevatedButton("Agregar cliente", icon="Check_circle")
_edit_button = ft.ElevatedButton("Editar cliente", icon="Edit")
_delete_button = ft.ElevatedButton("Eliminar cliente", icon="Delete")

_table = ft.DataTable(
    sort_column_index=0,
    sort_ascending=False,
    # Posibles columnas a agregar: RFC
    columns=[
        ft.DataColumn(ft.Text('ID'), numeric=True, on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
        ft.DataColumn(ft.Text('NOMBRE')),
        ft.DataColumn(ft.Text('APELLIDO')),
        ft.DataColumn(ft.Text('EDAD')),
        ft.DataColumn(ft.Text('CORREO ELECTRONICO')),
    ],
    rows=[
        # Add rows with client data here
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('5')),
                ft.DataCell(ft.Text('Yael')),
                ft.DataCell(ft.Text('Montes')),
                ft.DataCell(ft.Text('20')),
                ft.DataCell(ft.Text('jy@gmail.com'))
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('2')),
                ft.DataCell(ft.Text('Jose')),
                ft.DataCell(ft.Text('Montes')),
                ft.DataCell(ft.Text('23')),
                ft.DataCell(ft.Text('jy@gmail.com'))
            ]
        )
    ]
)
        
CustomerSection = ft.Column(
    controls=[
        ft.Text("Customers"),
        ft.Row(
            [
                ft.Icon(name=ft.icons.PERSON),
                ft.Text('Clientes', size=25),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                _search_bar,
            ],
            alignment=ft.MainAxisAlignment.END
        ),
        ft.Row(
            [
                _add_button, _edit_button, _delete_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                _table,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ]
)
