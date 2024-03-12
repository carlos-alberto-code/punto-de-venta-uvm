import flet as ft
from ..components.navs import Sidebar, AppBar, NavBar


# Aquí se definen los controles del sidebar de esta vista
_sidebar_controls = (
    ft.NavigationDrawerDestination(icon=ft.icons.ARTICLE, label="Compras"), # Sección a la que se accede por default cuando se selecciona compras en las opciones del navbar
    ft.NavigationDrawerDestination(icon=ft.icons.DATA_SAVER_OFF, label="Reportes"),
    ft.NavigationDrawerDestination(icon=ft.icons.STORAGE, label="Inventario"),
)

# Aquí se definen los destinos de la barra de navegación de esta vista
_navigation_destinations = (
    ft.NavigationDestination(icon=ft.icons.ARTICLE, label="Compras"),
    ft.NavigationDestination(icon=ft.icons.DATA_SAVER_OFF, label="Reportes"),
    ft.NavigationDestination(icon=ft.icons.STORAGE, label="Inventario"),
)

class PurchaseView(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self._sidebar_controls = _sidebar_controls

    def build(self):
        return ft.View(
            route="purchase/",
            appbar=AppBar(self._page).build(),
            drawer=Sidebar(*self._sidebar_controls).build(),
            navigation_bar=NavBar(*_navigation_destinations).build(),
            controls=[
                ft.Text("Content of Purchase View")
            ]
        )

