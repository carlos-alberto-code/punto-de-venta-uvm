from typing import List
import flet as ft
from .navigation_structure import Rail, Section
from ..theme.theme_config import ThemeMode

class ViewTemplate(ft.UserControl):
    def __init__(self, page: ft.Page, modules: dict[int, Rail]) -> None:
        super().__init__()
        self._page = page
        self._modules = modules
        self._sections: List[ft.NavigationDrawerDestination] = [section.build() for section in self._modules[0].sections]
        self._view = None

    def update_sections(self, event) -> None:
        index = event.control.selected_index
        rail = self._modules[index]
        sections = rail.sections
        self._sections = [section.build() for section in sections]
        self._view.drawer.controls = self._sections # type: ignore
        self._page.update()

    def build(self):
        # Construcción de la plantilla
        self._view = ft.View(
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
                    *self._sections,
                    ft.Divider(),
                    ft.NavigationDrawerDestination(icon='settings', label='Configuración'),
                    ft.NavigationDrawerDestination(icon=ft.icons.EXIT_TO_APP, label='Cerrar sesión')
                ]
            ),
            navigation_bar=ft.NavigationBar(
                destinations=[rail.build() for rail in self._modules.values()],
                on_change=self.update_sections,
            ),
        )
        return self._view
