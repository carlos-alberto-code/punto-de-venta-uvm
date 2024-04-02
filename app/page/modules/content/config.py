import flet as ft

_texto = ft.Text('Configuración')

ConfigContent = ft.AlertDialog(
    open=True,
    title=_texto,
    content=ft.Column(
        controls=[
            ft.Text('Aquí se mostrará la configuración de la aplicación.'),
            ft.Text('Por el momento, no hay nada que configurar.'),
            ft.DatePicker(
                
            )
        ]
    ),
    actions=[
        ft.ElevatedButton('Aceptar', on_click=lambda event: event.page.window_close()),
        ft.ElevatedButton('Cancelar', on_click=lambda event: event.page.window_close()),
    ],
)