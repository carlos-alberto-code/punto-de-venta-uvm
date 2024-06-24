import flet as ft

from views.AppView      import AppView
from views.LoginView    import LoginView
from theme.theme_config import LightTheme


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme      = LightTheme
    
    loging_view = LoginView(page)
    page.views.append(loging_view)
    # page.views.append(AppView(page))
    page.go(loging_view.route)
    


    
ft.app(main)