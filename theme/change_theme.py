import flet as ft
from theme.theme_config import LightTheme,DarkTheme
def change_icon(event: ft.ControlEvent):
    icon: ft.IconButton = event.control
    
    if icon.icon == ft.icons.LIGHT_MODE:
        icon.icon = ft.icons.DARK_MODE
        icon.update()
    else:
        icon.icon = ft.icons.LIGHT_MODE
        icon.update()

def change_theme(event: ft.ControlEvent):
    change_icon(event=event)
    page: ft.Page = event.page
    
    if page.theme_mode == ft.ThemeMode.LIGHT:
        page.theme_mode = ft.ThemeMode.DARK
        page.theme = DarkTheme
        page.update()
    else:
        page.theme_mode = ft.ThemeMode.LIGHT
        page.theme = LightTheme
        page.update()