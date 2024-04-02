import flet as ft

class CustomersModule(ft.UserControl):

    def __init__(self):
        super().__init__()
    
    def build(self):
        # Create search bar
        self.search_bar = ft.TextField(hint_text="Buscar cliente", width=200, height=50, icon=ft.icons.SEARCH)
        
        # Create buttons
        self.add_button = ft.ElevatedButton("Agregar cliente", icon="Check_circle")
        self.edit_button = ft.ElevatedButton("Editar cliente", icon="Edit")
        self.delete_button = ft.ElevatedButton("Eliminar cliente", icon="Delete")

        # Create table
        self.table = ft.DataTable(
            sort_column_index=0,
            sort_ascending=False,
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
        
        return ft.Column(
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
                        # self.search_bar,
                    ],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Row(
                    [
                        self.add_button, self.edit_button, self.delete_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        self.table,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        )
