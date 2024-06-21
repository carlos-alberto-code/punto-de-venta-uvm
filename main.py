import flet as ft
from views.LoginView import LoginView


def main(page: ft.Page):
    
    login_view  = LoginView(page)
    
ft.app(main)