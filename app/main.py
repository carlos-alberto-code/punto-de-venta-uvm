import flet as ft

from views.theme.theme_config import ThemeMode, LightTheme

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme

    page.add(ThemeMode(page))

ft.app(target=main)
