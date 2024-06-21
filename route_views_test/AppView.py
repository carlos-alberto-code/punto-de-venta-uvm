import flet as ft


class AppView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = 'app/'
        self.controls = [
            ft.Text('App View', size=20, weight=ft.FontWeight.BOLD, color='green'),
        ]