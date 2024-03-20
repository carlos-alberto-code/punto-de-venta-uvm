from .navigation_components import Appbar, Navbar, Drawer
from .events import ScreenEventHandlers
from .module import Module


from typing import List
import flet as ft


class NavegationScreen(ft.UserControl):
    """
    La pantalla de navegación es un componente fijo que sólo se recarga
    cuando se navega entre módulos. Al cambiar de módulo se renderizan nuevas secciones.
    Este componente sólo se recargará completamente cuando se haga un cambio de usuario.
    """

    screen_event_handlers = ScreenEventHandlers()

    def __init__(self, page: ft.Page, modules: List[Module]):
        super().__init__()
        self._page = page
        self._view: ft.View # Declaramos para entender que existe
        self._modules = modules
        self._appbar = Appbar(page)
        self._navbar = Navbar(
            page,
            [module.rail.build() for module in self._modules],
            self.screen_event_handlers.update_sections
        )
        self._drawer = Drawer(page)
    
    @property
    def modules(self) -> List[Module]:
        return self._modules
    
    @modules.setter
    def modules(self, modules: List[Module]):
        self._modules = modules

    def build(self):
        self._view = ft.View(
            appbar=self._appbar.build(),
            drawer=self._drawer.build(),
            navigation_bar=self._navbar.build(),
        )
        return self._view