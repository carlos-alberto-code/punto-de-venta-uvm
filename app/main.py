import flet as ft

from view.navigation.appbar_controls import AppbarActions
from view.navigation.appbar import Appbar
# from view.modules.modules_declaration import module

def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.DARK  # Se remplaza por las preferencias de usuario

    # Appbar: Construcción inicial del appbar
    appbar_actions = AppbarActions(page.theme_mode)
    appbar = Appbar(actions=appbar_actions.controls).build()
    page.appbar = appbar

    page.update()


ft.app(target=main)