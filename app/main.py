from time import sleep
import flet as ft

from page.modules import modules
from page.navigation.initializer import Initializer
from page.navigation.appbar_controls import AppbarActions
from page.navigation.navigation_structures import NavigationStructureFactory


def main(page: ft.Page):

    mods    = modules.Module.all_modules
    init    = Initializer(modules=mods, navbar_index=1, drawer_index=0)
    struct  = NavigationStructureFactory(initializer=init)

    page.window_maximized       = True
    page.scroll                 = ft.ScrollMode.AUTO
    page.theme_mode             = ft.ThemeMode.LIGHT
    # page.vertical_alignment     = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment   = ft.CrossAxisAlignment.CENTER

    content = init.initial_drawer_section_content
    page.add(content)

    page.navigation_bar = struct.navbar
    page.drawer         = struct.drawer
    page.appbar         = struct.appbar(AppbarActions().controls)
    page.update()

    sleep(1.5)
    page.drawer.open = False
    page.update()


ft.app(target=main)
