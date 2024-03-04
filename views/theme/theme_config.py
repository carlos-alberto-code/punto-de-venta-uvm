from .paletts import _light_color_palette, _dark_color_palette
from .text_theme_config import text_theme

import flet as ft


def change_theme(e):
    theme_mode = e.theme_mode
    if theme_mode == ft.ThemeMode.LIGHT:
        _change_to_dark_theme(e)
    if theme_mode == ft.ThemeMode.DARK:
        _change_to_light_theme(e)

# Configuración del tema claro
def _change_to_light_theme(page: ft.Page):
    page.bgcolor = light_theme.color_scheme.background
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = light_theme
    page.update()

light_theme = ft.Theme(
    color_scheme=ft.ColorScheme(**_light_color_palette),
    text_theme=text_theme
)


# Configuración del tema oscuro
def _change_to_dark_theme(page: ft.Page):
    page.bgcolor = dark_theme.color_scheme.background
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = dark_theme
    page.update()

dark_theme = ft.Theme(
    color_scheme=ft.ColorScheme(**_dark_color_palette),
    text_theme=text_theme
)
