from typing import List
import flet as ft

from .events import update_module, update_content
from .appbar_controls import AppbarActions
from .builder import Module


class NavigationComponentsFactory:
    # TODO: Falta construir el contenido de la página

    def __init__(self, modules: List[Module]) -> None:
        if not modules:
            raise ValueError('No se han proporcionado módulos. La lista está vacía')
        self._appbar_actions = AppbarActions().controls
        self.modules = modules
        self.index = 4
        self._build_initial_content()

    def _initial_module(self) -> Module:
        if self.index < 0 or self.index >= len(self.modules):
            raise IndexError('El índice para acceder al módulo está fuera del rango de los módulos que existen.')
        return self.modules[self.index]
    
    def _build_initial_content(self):
        return []

    def build_navigation_bar(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            selected_index=self.index,
            destinations=[module.rail.build() for module in self.modules],
            on_change=update_module,
        )
    
    def build_appbar(self) -> ft.AppBar:
        return ft.AppBar(
            title=ft.Text(f'{self._initial_module().name}'),
            center_title=True,
            actions=self._appbar_actions,
        )
    
    def build_drawer(self) -> ft.NavigationDrawer:
        return ft.NavigationDrawer(
            selected_index=0,
            controls=[control.build() for control in self._initial_module().sections],
            on_change=update_content,
        )