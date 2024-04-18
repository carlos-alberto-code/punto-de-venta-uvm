from typing import List
from time import sleep

import flet as ft

from .navigation_state import NavigationStateManager
from .events import update_module, update_content
from .appbar_controls import AppbarActions
from .builder import Module

class NavigationComponentsFactory:

    NAVBAR_INDEX = 1
    DRAWER_INDEX = 1

    def __init__(self, modules: List[Module]) -> None:
        if not modules:
            raise ValueError('No se han proporcionado módulos. La lista está vacía')
        self.modules = modules

        self.navigation_state_manager = NavigationStateManager()
        self.navigation_state_manager.modules = modules
        
        self.initial_module = Initializer(modules, self.NAVBAR_INDEX).initial_module()

    def build_navigation_bar(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            selected_index=self.NAVBAR_INDEX,
            destinations=self._build_navigation_bar_controls(),
            on_change=update_module,
        )
    
    def _build_navigation_bar_controls(self) -> List[ft.NavigationDestination]:
        return [module.rail for module in self.modules]
    
    def build_appbar(self) -> ft.AppBar:
        return ft.AppBar(
            title=ft.Text(f'{self.initial_module.name}'),
            center_title=True,
            actions=AppbarActions().controls,
        )
    
    def build_drawer(self) -> ft.NavigationDrawer:
        return ft.NavigationDrawer(
            selected_index=self.DRAWER_INDEX,
            controls=self._build_drawer_controls(),
            on_change=update_content,
        )
    
    def _build_drawer_controls(self) -> List[ft.Control]:
        return [control for control in self.initial_module.sections]
    
    def build_content(self, page: ft.Page) -> None:
        page.drawer.open = True # type: ignore
        content = self.initial_module.sections[self.DRAWER_INDEX].content
        page.add(content)
        sleep(2)
        page.drawer.open = False # type: ignore





class Initializer:

    def __init__(self, modules: List[Module], index: int) -> None:
        self._modules = modules
        self._index = index
        
    
    def initial_module(self) -> Module:
        if self._index < 0 or self._index >= len(self._modules):
            raise IndexError('El índice para acceder al módulo está fuera del rango de los módulos que existen.')
        return self._modules[self._index]
    
    
