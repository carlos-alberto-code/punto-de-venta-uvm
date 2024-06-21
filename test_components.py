import flet as ft
from roles.login import Login
from roles.session import Session



def main(page: ft.Page):
    
    Login(page)

ft.app(main)