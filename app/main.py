from time import sleep

import flet as ft

from page.navigation.navigation_structures import NavigationStructureFactory
from page.navigation.initializer import Initializer
from page.navigation.module import Module
from page.modules import (
    purchase_module,
    inventory_module,
    pos_module,
    sales_module,
)


def main(page: ft.Page):

    modules = Module.all_modules
    init    = Initializer(modules=modules, navbar_index=3, drawer_index=0)
    struct  = NavigationStructureFactory(initializer=init)

    page.window_maximized       = True
    page.scroll                 = ft.ScrollMode.AUTO
    page.vertical_alignment     = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment   = ft.CrossAxisAlignment.CENTER

    content = init.initial_drawer_section_content
    page.add(content)

    page.navigation_bar = struct.navbar
    page.drawer         = struct.drawer
    page.appbar         = struct.appbar()
    page.update()

    sleep(1.5)
    page.drawer.open = False
    page.update()




ft.app(target=main)
