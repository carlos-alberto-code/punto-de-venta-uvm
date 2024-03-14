import flet as ft
from ..components.navs import AppBar, NavBar, Sidebar


# Aquí se definen los controles del sidebar de esta vista
_sidebar_controls = (
    ft.NavigationDrawerDestination(icon=ft.icons.ARTICLE, label="Compras"), # Sección a la que se accede por default cuando se selecciona compras en las opciones del navbar
    ft.NavigationDrawerDestination(icon=ft.icons.DATA_SAVER_OFF, label="Reportes"),
    ft.NavigationDrawerDestination(icon=ft.icons.STORAGE, label="Inventario"),
)

# Aquí se definen los destinos de la barra de navegación de esta vista
_navigation_destinations = (
    ft.NavigationDestination(icon=ft.icons.ARTICLE, label="Compras"),
    ft.NavigationDestination(icon=ft.icons.STORE_MALL_DIRECTORY, label="Inventario"),
    ft.NavigationDestination(icon=ft.icons.MONEY, label="Ventas"),
    ft.NavigationDestination(icon=ft.icons.DATA_SAVER_OFF, label="Reportes"),
    ft.NavigationDestination(icon=ft.icons.PEOPLE, label="Clientes"),
    ft.NavigationDestination(icon=ft.icons.LOCATION_ON, label="Sucursales"),
)

class PurchaseModuleView(ft.UserControl):
    # Al tener secciones específicas, esta vista sirve sólo para manejar el enrutamiento a esas otras secciones
    # Cada sección tendrá el contenido específico para construir la vista que le corresponde.

    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self._sidebar_controls = _sidebar_controls

    def build(self):
        return ft.View(
            route="purchases/",
            appbar=AppBar(self._page).build(),
            drawer=Sidebar(*self._sidebar_controls).build(),
            navigation_bar=NavBar(*_navigation_destinations).build(),
            controls=[
                ft.ElevatedButton(text='Abrir configuración')
            ]
        )

