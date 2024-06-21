import flet as ft
from business_classes.user  import User


class AppView(ft.View):

    def __init__(self, page: ft.Page, user: User):
        super().__init__()
        self.route: str = 'app/'
        if user.theme_mode == 'light':
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.window.maximized = True
        # page.window.frameless = True
        page.padding = 0
        page.add(ft.Text('Bienvenido', size=20, weight=ft.FontWeight.BOLD))
        page.update()