from views.theme.theme_config import ThemeMode, LightTheme
import flet as ft



def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = LightTheme.color_scheme.background # type: ignore
    page.theme = LightTheme

    page.add(ThemeMode(page))
    
ft.app(main)
