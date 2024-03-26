import flet as ft

from view.navigation.controls import AppbarControls

def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE


    # Appbar
    page.appbar = ft.AppBar(
        title=AppbarControls.central_controls(title='Compras'),
        actions=AppbarControls.action_controls()
    )

    # Navbar
    page.navigation_bar = ft.NavigationBar(
        destinations=[]
    )

    # Drawer
    page.drawer = ft.NavigationDrawer(

    )

    page.update()

ft.app(target=main)
