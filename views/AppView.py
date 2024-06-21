import flet as ft
from business_classes.user  import User
from typing import Optional


class AppView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.__screen = page
        self.route: str = 'app/'
        self.__user: Optional[User] = None
        
    
    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user: User):
        self.__user = user
        self.build_view()
        
    def build_view(self):
        if self.__user:
            if self.__user.theme_mode == 'light':
                self.__screen.theme_mode = ft.ThemeMode.LIGHT
            else:
                self.__screen.theme_mode = ft.ThemeMode.DARK
            self.__screen.window.maximized = True
            self.__screen.window.frameless = True
            self.__screen.padding = 0
            self.__screen.clean()
            self.__screen.add(ft.Text(f'Bienvenido {self.__user.username.title()}', size=20, weight=ft.FontWeight.BOLD))
            self.__screen.update()