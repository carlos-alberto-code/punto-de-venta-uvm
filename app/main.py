import flet as ft

from view.navigation.appbar_controls import AppbarActions
from view.navigation.appbar import Appbar
# from view.modules.modules_declaration import module

def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.DARK  # Se remplaza por las preferencias de usuario

    # Appbar: Construcción inicial del appbar
    appbar_actions = AppbarActions(page.theme_mode).controls # No hay setter, pues no debe permitir el cambio de controles.
    appbar = Appbar(title=ft.ElevatedButton('Send'), actions=appbar_actions).build()
    page.appbar = appbar

    """
    NOTE: En el enfoque actual, el appbar se reconstruye completamente se puede hacer de dos maneras.
    Haciendo la reconstrucción en una función que se implemente justo como se inicializa, o bien,
    modificando la variable que tiene el appbar con el metodo build, pues es en la construcción donde
    los cambios surten efecto. Luego podemos inyectar los cambios en page.appbar.
    """

    page.update()


ft.app(target=main)