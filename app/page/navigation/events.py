from .drawer_controls import DrawerControls
from .builder import Module, Section
from typing import List
import flet as ft


def update_module(event: ft.ControlEvent): # Actualiza el módulo seleccionado en el Navbar
    event.page.clean()
    index = event.control.selected_index
    module = Module.all_modules[index]
    # Actualiza el título del AppBar
    event.page.appbar.title = ft.Text(module.name)
    # Actualiza los controles del Drawer
    central_controls: List[ft.Control] = [control.build() for control in module.sections]
    event.page.drawer.controls = DrawerControls.load_controls(central_controls)
    event.page.drawer.selected_index = 1
    event.page.drawer.open = True
    event.page.update()


def update_content(event: ft.ControlEvent): # Actualiza el contenido de la sección del Drawer
    # Determinar en qué módulo estamos
    module_index = event.page.navigation_bar.selected_index
    module = Module.all_modules[module_index]
    # Preparar la lista de secciones de este módulo
    sections = module.sections
    # Determinar en qué sección estamos
    drawer_index = event.control.selected_index
    section = sections[0] # Selecciono esté, por que los demás están fuera del rango.
    # Agregar los controles de section.content a la pagina
    event.page.add(section.content)
    event.page.drawer.open = False
    event.page.update()
    # TODO: Creo entender el error.
    # El error se da por que la tupla que contiene las secciones es una tupla que proviene de fuera
    # Entonces, los controles del drawer, son otra lista, y las secciones vienen a añadirse
    # Con lo cual, cuando se da un clic en una sección que proviene del módulo, está no estará
    # en el radar de la lista de controles del drawer, por eso da un tuple index out of range
