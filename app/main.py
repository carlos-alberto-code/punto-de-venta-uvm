import flet as ft


from page.navigation.components import NavigationComponentsFactory

from page.navigation.builder import Module
from page.modules import (
    purchase_module,
    inventory_module,
    pos_module,
    sales_module,
    customer_module
)


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT  # Se remplaza por las preferencias de usuario

    # Un paso previo es la devolución de módulos en función del rol de usuario
    modules = Module.all_modules
    nav_components = NavigationComponentsFactory(modules)

    page.navigation_bar = nav_components.build_navigation_bar()
    page.appbar = nav_components.build_appbar()
    page.drawer = nav_components.build_drawer()

    page.update()


ft.app(target=main)
