import flet as ft
from views.LoginView import LoginView


def main(page: ft.Page):
    
    # TODO: Verificar la base de datos para ver si hay un usuario con sesión iniciada. No puede haber más de un usuario con sesión iniciada. Si hay un usuario con sesión iniciada, se devuelve ese usuario y se verifica si el usuario ha indicado que se recuerde su sesión. Si el usuario ha indicado que se recuerde su sesión, se inicia sesión automáticamente. Si el usuario no ha indicado que se recuerde su sesión, se muestra la página de inicio de sesión para que pueda iniciar sesión manualmente.

    login_view  = LoginView(page)
    
ft.app(main)