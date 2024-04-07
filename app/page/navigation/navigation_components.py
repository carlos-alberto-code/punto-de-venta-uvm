import flet as ft


class NavigationComponentsFactory:

    def create_appbar(self):
        return ft.AppBar()
    
    def create_navigation_bar(self):
        return ft.NavigationBar()
    
    def create_drawer(self):
        return ft.NavigationDrawer()