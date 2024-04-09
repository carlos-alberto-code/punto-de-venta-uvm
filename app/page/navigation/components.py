from typing import List

import flet as ft

from .events import update_module, update_content
from .appbar_controls import AppbarActions
from .builder import Module

class NavigationComponentsFactory:
    # TODO: Falta construir el contenido de la página inicial

    def __init__(self, modules: List[Module]) -> None:
        if not modules:
            raise ValueError('No se han proporcionado módulos. La lista está vacía')
        self.modules = modules
        self.destination_index = 0
        self.drawer_index = 0

    def _initial_module(self) -> Module:
        if self.destination_index < 0 or self.destination_index >= len(self.modules):
            raise IndexError('El índice para acceder al módulo está fuera del rango de los módulos que existen.')
        return self.modules[self.destination_index]
    
    def _initial_section(self):
        return self._initial_module().sections[self.drawer_index]
    
    def initial_content(self) -> ft.Control:
        return self._initial_section().content

    def build_navigation_bar(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            selected_index=self.destination_index,
            destinations=[module.rail.build() for module in self.modules],
            on_change=update_module,
        )
    
    def build_appbar(self) -> ft.AppBar:
        return ft.AppBar(
            title=ft.Text(f'{self._initial_module().name}'),
            center_title=True,
            actions=AppbarActions().controls,
        )
    
    def build_drawer(self) -> ft.NavigationDrawer:
        return ft.NavigationDrawer(
            selected_index=self.drawer_index,
            controls=[control.build() for control in self._initial_module().sections],
            on_change=update_content,
        )

    def set_modules(self, modules: List[Module]) -> None:
        self.modules = modules
        self.destination_index = 0
        #self.initial_content()