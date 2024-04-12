import flet as ft

from page.login import LoginPage


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT  # Se remplaza por las preferencias de usuario

    page.add(LoginPage(page).build())


ft.app(target=main)
