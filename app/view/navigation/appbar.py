from typing import List
import flet as ft

# Este componente subfrirá cambios dinámicos en función de eventos de cambio en ciertos controles Flet.
# Por ejemplo, el botón de tema cambiará su icono dependiendo del tema actual.
# El título de la barra de aplicaciones también puede cambiar dinámicamente.
# Habrá unos controles que deben estar siempre presentes, como el botón de cierre.
# Pero el enfoque que se adoptará aquí es que todos los controles se inyecten siempre que haya un evento de cambio.
class Appbar(ft.UserControl):

    def __init__(self, actions: List[ft.Control] = []):
        self.actions = actions

    def build(self):
        return ft.AppBar(
            actions=self.actions
        )