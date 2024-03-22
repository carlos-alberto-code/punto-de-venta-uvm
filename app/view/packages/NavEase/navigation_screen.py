from ...modules.create import create_modules
from .navigation_components import Appbar, Navbar, Drawer
import flet as ft


class NavScreen(ft.UserControl):
    """
    La pantalla de navegación es un componente fijo que sólo se recarga
    cuando se navega entre módulos. Al cambiar de módulo se renderizan nuevas secciones.
    Este componente sólo se recargará completamente cuando se haga un cambio de usuario.
    """


    def __init__(self, page: ft.Page):
        # No debe saber qué módulos existen, sólo debe saber cómo mostrarlos.
        super().__init__()
        self._page = page

    def build(self):
        self.appbar = Appbar()
        self.drawer = Drawer()
        self.navbar = Navbar(create_modules())
        self.navbar.register(self.drawer)
        return ft.View(
            appbar=self.appbar.build(),
            drawer=self.drawer.build(),
            navigation_bar=self.navbar.build()
        )