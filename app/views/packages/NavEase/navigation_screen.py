from .navigation_components import Appbar, Navbar, Drawer
from ...modules.create import create_modules
from .module import Module

from typing import List
import flet as ft


class NavegationScreen(ft.UserControl):
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
        self._appbar = Appbar(page=self._page).build()
        self._drawer = Drawer()
        self._navbar = Navbar(create_modules())
        self._navbar.register(self._drawer)
        self._navbar = self._navbar.build()
        self._drawer = self._drawer.build()
        return ft.View(
            appbar=self._appbar,
            drawer=self._drawer,
            navigation_bar=self._navbar
        )