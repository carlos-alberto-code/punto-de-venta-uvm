import flet as ft
from modules import Module
from roles.user import User

carlos = User(username='carlos', password='1234', modules=[Module.repo['Tienda']])
yael = User(
    username='yael',
    password='1234',
    modules=[
        Module.repo['Tienda'],
        Module.repo['Productos'],
        Module.repo['Compras'],
        Module.repo['Proveedores'],
    ]
)


def main(page: ft.Page):

    def handle_on_change(event: ft.ControlEvent):
        index = event.control.selected_index
        modules = user.modules
        for i, module in enumerate(modules):
            if i == index:
                shape.controls[1] = module.content
                shape.update()
                break
        

    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.maximized = True
    page.padding = 0

    user = yael

    rail = ft.NavigationRail(
        col=1.20,
        elevation=30,
        group_alignment=-0.9,
        destinations=[*user.modules],
        on_change=handle_on_change,
    )

    home = ft.Container(
        col=10.80,
        padding=15,
        content=ft.Column(
            [
                ft.Text(value='Bienvenido', size=30),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    shape = ft.ResponsiveRow(
            controls=[
                rail,
                home,
            ],
            expand=True,
            col=12,
        )
   
    page.add(shape)

ft.app(main)