import flet as ft

from views.theme.theme_config import LightTheme, DarkTheme # Tema
from views.modules.create import create_modules
from views.packages.NavEase.navigation_screen import NavegationScreen


def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = LightTheme.color_scheme.background # type: ignore

    # Creación de la vista
    screen = NavegationScreen(page, create_modules())
    page.views.append(screen.build())
    
    page.update()

    

ft.app(target=main)
