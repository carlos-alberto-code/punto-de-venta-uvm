import flet as ft

from page.navigation.navigation_components import NavigationComponentsFactory
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

    page.window_maximized = True
    page.window_frameless = True

    # Un paso previo es la devolución de módulos en función del rol de usuario
    modules = Module.all_modules
    factory = NavigationComponentsFactory(modules)

    page.appbar         = factory.build_appbar()
    page.drawer         = factory.build_drawer()
    page.navigation_bar = factory.build_navigation_bar()

    factory.build_content(page)

    page.update()


ft.app(target=main)
