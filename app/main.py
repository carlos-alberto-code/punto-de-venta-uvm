import flet as ft

from views.theme.theme_config import LightTheme, DarkTheme # Tema
from views.packages.NavEase.navigation_screen import NavScreen


def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = LightTheme.color_scheme.background # type: ignore

    screen = NavScreen(page)
    page.views.append(screen.build())
    
    page.update()

    

ft.app(target=main)
