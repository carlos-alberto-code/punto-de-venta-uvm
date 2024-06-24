import flet as ft

from views.AppView      import AppView
from views.LoginView    import LoginView
from theme.theme_config import LightTheme, DarkTheme


def main(page: ft.Page):

    # TODO: Verificar la base de datos para ver si hay un usuario con sesión iniciada. No puede haber más de un usuario con sesión iniciada. Si hay un usuario con sesión iniciada, se devuelve ese usuario y se verifica si el usuario ha indicado que se recuerde su sesión. Si el usuario ha indicado que se recuerde su sesión, se inicia sesión automáticamente. Si el usuario no ha indicado que se recuerde su sesión, se muestra la página de inicio de sesión para que pueda iniciar sesión manualmente.
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme
    page.title = 'Punto de venta'

    page.views.append(LoginView(page))
    page.views.append(AppView(page))
    
ft.app(main)