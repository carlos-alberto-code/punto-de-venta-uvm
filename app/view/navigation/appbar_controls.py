from typing import List
import flet as ft

# Icons
_light_mode  = ft.icons.LIGHT_MODE
_dark_mode   = ft.icons.DARK_MODE
_close       = ft.icons.CLOSE


def _toggle_theme(event: ft.ControlEvent):
    # Toggle the theme
    event.page.theme_mode = ft.ThemeMode.DARK if event.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
    # Update the icon to match the new theme
    event.control.icon = _light_mode if event.page.theme_mode == ft.ThemeMode.DARK else _dark_mode
    # Update the page to apply the new theme
    event.page.update()

theme_button = ft.IconButton(icon=_light_mode, on_click=_toggle_theme)


def _close_app(event: ft.ControlEvent):
    event.page.window_close()

close_button = ft.IconButton(icon=_close, on_click=_close_app)


"""
NOTE: En caso de necesitarse más controles, este es el lugar en el que se declaran,
junto con sus eventos.
"""