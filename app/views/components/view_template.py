from ..theme.theme_config import ThemeMode
from ..packages.NavEase.module import Rail, Section

from typing import List
import flet as ft



class ViewTemplate(ft.UserControl):
    def __init__(self, page: ft.Page, modules: dict[int, Rail]) -> None:
        super().__init__()
        self._page = page
        self.appbar = Appbar(self._page)
        self.drawer = Drawer(self._page)
        self.navigation_bar = NavigationBar(self._page)
        self._modules = modules
        self._sections: List[ft.NavigationDrawerDestination] = [section.build() for section in self._modules[0].sections]
        self._view = None
    
    def check_initial_module(self):
        pass

    def update_sections(self, event) -> None:
        index = event.control.selected_index
        rail = self._modules[index]
        sections = rail.sections
        self._sections = [section.build() for section in sections]
        self._view.drawer.controls = self._sections # type: ignore
        self._page.update()
    
    def build_appbar(self):
        return ft.AppBar(
            actions=[
                ThemeMode(self._page),
                ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda _: self._page.window_close())
            ]
        )
    
    def build_navigation_bar(self):
        return ft.NavigationBar(
            destinations=[rail.build() for rail in self._modules.values()],
            on_change=self.update_sections,
        )
    
    def build_drawer(self):
        return ft.NavigationDrawer(
            selected_index=1,
            controls=[
                ft.Container(height=14),
                ft.NavigationDrawerDestination(icon='person', label='Usuario'),
                ft.Divider(),
                *self._sections,
                ft.Divider(),
                ft.NavigationDrawerDestination(icon='settings', label='Configuración'),
                ft.NavigationDrawerDestination(icon=ft.icons.EXIT_TO_APP, label='Cerrar sesión')
            ]
        )


    def build(self):
        # Construcción de la plantilla
        self._view = ft.View(
            appbar=self.appbar.build(),
            drawer=self.drawer.build(),
            navigation_bar=self.navigation_bar.build(),
        )
        return self._view