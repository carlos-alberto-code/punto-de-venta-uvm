import flet as ft

from ..theme.theme_config import ThemeMode


class Sidebar(ft.UserControl):

    def __init__(self, *destinations: ft.NavigationDrawerDestination):
        super().__init__()
        self._destinations = destinations

    def build(self):
        return ft.NavigationDrawer(
            controls=[
                ft.Container(height=14),
                ft.NavigationDrawerDestination(icon=ft.icons.PERSON, label="Perfil"),
                ft.Divider(height=15),
                *[dest for dest in self._destinations],
                ft.Divider(height=15),
                ft.NavigationDrawerDestination(icon=ft.icons.SETTINGS, label="Configuración"),
                ft.NavigationDrawerDestination(icon=ft.icons.ARROW_DOWNWARD, label="Cerrar Sesión"),
            ]
        )


class AppBar(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page

    def build(self):
        return ft.AppBar(
            actions=[
                ThemeMode(self._page),
                ft.IconButton(icon=ft.icons.CLOSE,)
            ]
        )


class NavBar(ft.UserControl):
    
        def __init__(self, *destinations: ft.NavigationDestination):
            super().__init__()
            self._destinations = destinations # Los destinos dependen de los permisos de usuario
    
        def build(self):
            return ft.NavigationBar(
                destinations=[
                    *[dest for dest in self._destinations]
                ]
            )