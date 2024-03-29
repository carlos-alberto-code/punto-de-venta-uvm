import flet as ft


content = ft.Column(
    controls=[
        ft.Text('Proveedores'),
        ft.Text('Aquí se listarán los proveedores.'),
        ft.ElevatedButton('Agregar proveedor', on_click=lambda event: print('Agregar proveedor'))
    ]
)