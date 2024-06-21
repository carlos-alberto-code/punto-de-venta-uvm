import flet as ft
from modules import Module
from roles.user import User
from home_content import HomeContent
from roles.login import Login
from theme.theme_config import LightTheme, DarkTheme
from theme.change_theme import change_theme


carlos = User(
    username='carlos',
    password='1234',
    modules=[
        Module.repo['Tienda'],
        Module.repo['Productos'],
        Module.repo['Compras'],
        Module.repo['Proveedores'],
    ]
)
yael = User(
    username='yael',
    password='1234',
    modules=[
        Module.repo['Tienda'],
        Module.repo['Productos'],
        Module.repo['Compras'],
    ]
)


def main(page: ft.Page):

    # page.add(Login(page))


    def handle_on_change(event: ft.ControlEvent):
        index = event.control.selected_index
        modules = user.modules
        for i, module in enumerate(modules):
            if i == index:
                shape.controls[1] = module.content
                shape.update()
                appbar.title = ft.Text(module.name)
                appbar.update()
                break
        
    

    user = carlos

    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme
    page.window.maximized = True
    page.window.frameless = True
    page.padding = 0

    appbar = ft.AppBar(
        center_title=True,
        actions=[
            ft.IconButton(icon='dark_mode', tooltip='Cambiar tema', on_click=change_theme),
            ft.PopupMenuButton(
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(text='Perfil de usuario', icon='person'),
                    ft.PopupMenuItem(text='Configuración', icon='settings'),
                    ft.PopupMenuItem(text='Cerrar sesión', icon='logout', on_click=lambda e: page.window.close()),
                ]
            )
        ]
    )
    page.appbar = appbar


    rail = ft.NavigationRail(
        col=1.20,
        elevation=30,
        group_alignment=-1,
        destinations=[*user.modules],
        on_change=handle_on_change,
    )

    shape = ft.ResponsiveRow(
            controls=[
                rail,
                HomeContent(user=user.username),
            ],
            expand=True,
            col=12,
        )
   
    page.add(shape)

ft.app(main)
