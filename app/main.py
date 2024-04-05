import flet as ft

from page.navigation.drawer_controls import DrawerControls
from page.navigation.appbar_controls import AppbarActions

from page.navigation.events import update_module, update_content
from page.navigation.builder import Module
from page.modules import ( # El orden en el que se importan es el orden en que se mostrará en el Navbar
    purchase_module,
    inventory_module,
    pos_module,
    sales_module,
    customer_module,
)


def main(page: ft.Page):


    page.theme_mode = ft.ThemeMode.LIGHT  # Se remplaza por las preferencias de usuario

    
    modules = Module.all_modules


    # APPBAR

    appbar_actions = AppbarActions(page.theme_mode).controls
    page.appbar = ft.AppBar(
        title=ft.Text('Appbar'),
        center_title=True,
        actions=appbar_actions,
    )


    # NAVIGATIONBAR
    
    SELECTED_MODULE = 0
    page.navigation_bar = ft.NavigationBar(
        selected_index=SELECTED_MODULE,
        destinations=[module.rail.build() for module in modules],
        on_change=update_module,
    )


    # DRAWER

    SELECTED_SECTION = 1
    page.drawer = ft.NavigationDrawer(
        selected_index=SELECTED_SECTION,
        controls=DrawerControls.load_controls([]),
        on_change=update_content
    )

    page.update()


ft.app(target=main)
