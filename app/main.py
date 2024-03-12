import flet as ft

from views.theme.theme_config import ThemeMode, LightTheme, DarkTheme

def main(page: ft.Page):

    # page.window_title_bar_hidden = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme
    page.update()

ft.app(target=main)
