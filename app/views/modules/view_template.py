from typing import List, Dict
import flet as ft

from ..theme.theme_config import ThemeMode


class SectionView(ft.UserControl):
    """
    El propósito de este objeto es establecer los módulos y sus secciones, permitiendo cambiar en tiempo de ejecución
    en función del cambio de usuario.
    """

    def __init__(self, page: ft.Page, modules: Dict[ft.NavigationDestination, ft.NavigationDrawerDestination]):
        super().__init__()
        self._page = page
        self.modules: List[ft.NavigationDestination] = []
        self.sections: List[ft.NavigationDrawerDestination] = []
    
    def build(self):
        return ft.View(
            appbar=ft.AppBar(
                actions=[
                    ThemeMode(self._page),
                    ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda _: self._page.window_close())
                ]
            ),
            drawer=ft.NavigationDrawer(
                selected_index=1,
                controls=[
                    ft.Container(height=14),
                    ft.NavigationDrawerDestination(icon='person', label='Usuario'),
                    ft.Divider(),
                    *self.sections,
                    ft.Divider(),
                    ft.NavigationDrawerDestination(icon='settings', label='Configuración'),
                    ft.NavigationDrawerDestination(icon=ft.icons.EXIT_TO_APP, label='Cerrar sesión')
                ]
            ),
            navigation_bar=ft.NavigationBar(
                selected_index=0,
                destinations=self.modules
                # on_change=
            ),
        )