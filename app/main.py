import flet as ft

from view.navigation import active_navs

def main(page: ft.Page):
    
    page.navigation_bar, page.drawer, page.appbar = active_navs()
    page.update()

ft.app(target=main)
