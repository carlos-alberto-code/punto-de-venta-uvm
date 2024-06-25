import flet as ft

from views.LoginView    import LoginView
from theme.theme_config import LightTheme


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme      = LightTheme
    
    page.views.append(LoginView(page))
    page.go('login/')
    
ft.app(main)
