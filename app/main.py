import flet as ft
from page.navigation.appbar_controls import AppbarActions
from page.modules.builder import Module

from page.modules import purchase_module, customer_module # Import all modules from the modules folder


def main(page: ft.Page):


    page.theme_mode = ft.ThemeMode.LIGHT  # Se remplaza por las preferencias de usuario


    # APPBAR

    appbar_actions = AppbarActions(page.theme_mode).controls
    page.appbar = ft.AppBar(
        title=ft.Text('Appbar'),
        center_title=True,
        actions=appbar_actions,
    )


    # NAVIGATIONBAR

    def update_module(event):
        print('Se actualizan los controles del Drawer y el título del Appbar.')
        pass
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[ft.NavigationDestination(label='Home')],
        on_change=update_module,
    )


    # DRAWER

    def update_content(event):
        print('Se actualiza el contenido')

    page.drawer = ft.NavigationDrawer(
        controls=[ft.NavigationDrawerDestination(label='User')],
        on_change=update_content
    )

    page.update()
    print(Module.all_modules)


ft.app(target=main)