from typing import List
import flet as ft


# EVENTOS PARA EL APPBAR

def change_theme(event) -> None:
    # Cambiar el tema de la aplicación
    pass

def close(event) -> None:
    # Cerrar la ventana
    event.page.window.close()


class Appbar(ft.UserControl):
    # Este componente es fijo, no cambia de acuerdo a la página

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self._page = page
        self.theme_mode_control = ft.IconButton(icon=ft.icons.LIGHT_MODE, on_click=change_theme)
        self.close_control = ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda _: self._page.window_close())

    def build(self):
        return ft.AppBar(
            actions=[
                self.theme_mode_control,
                self.close_control,
            ]
        )
    

class Navbar(ft.UserControl):
    # Este componentes es fijo, no cambia de acuerdo a la página, pero los
    # destinos tienen que cambiar de acuerdo con los permisos de usuario.
     
    def __init__(self, page: ft.Page, destinations: List[ft.NavigationDestination], event) -> None:
        super().__init__()
        self._page = page
        self.destinations = destinations
        self._event = event

    def build(self):
        return ft.NavigationBar(
            destinations=self.destinations,
            on_change=self._event,
        )


class Drawer(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self.sections: List[ft.NavigationDrawerDestination] = []

    def build(self):
        return ft.NavigationDrawer(
            controls=[
                ft.Container(height=14),
                ft.NavigationDrawerDestination(
                    label='Usuario',
                    icon=ft.icons.PERSON,
                ),
                ft.Divider(),
                *self.sections,
                ft.Divider(),
                ft.NavigationDrawerDestination(
                    label='Configuración',
                    icon=ft.icons.SETTINGS,
                ),
                ft.NavigationDrawerDestination(
                    label='Cerrar sesión',
                    icon=ft.icons.LOGOUT,
                ),
            ]
        )