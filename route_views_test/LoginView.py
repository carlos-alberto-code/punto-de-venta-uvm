from time import sleep
import flet as ft
from route_views_test.AppView import AppView


class LoginView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = 'login/'
        self.controls = [
            ft.Text('Login View', size=20, weight=ft.FontWeight.BOLD, color='blue'),
        ]
        page.views.append(AppView(page))
        sleep(5)
        page.go(str(AppView(page).route))