from .NavigationHandler import State

from time import sleep
from typing import List
import flet as ft


state = State()


def update_module(event: ft.ControlEvent):
    clean_page(event)
    destination_index = get_destination_index(event)
    module = state.get_module_from_destination_index(destination_index)
    update_appbar_title(event, module.name)
    update_drawer_controls(event, module)
    open_drawer(event)
    select_drawer_index(event, 0)
    event.page.add(get_controls_from_current_drawer_index(event))
    sleep(0.7)
    close_drawer(event)
    update_page(event)


def update_content(event: ft.ControlEvent): # Actualiza el contenido de la sección del Drawer
    # Determinar en qué módulo estamos
    module = state.get_current_module()
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





def clean_page(event: ft.ControlEvent) -> None:
    event.page.clean()

def get_destination_index(event: ft.ControlEvent) -> int:
    return event.page.navigation_bar.selected_index

def update_appbar_title(event: ft.ControlEvent, title: str) -> None:
    event.page.appbar.title = ft.Text(title)

def update_drawer_controls(event, module):
    event.page.drawer.controls = [control.build() for control in module.sections]

def open_drawer(event: ft.ControlEvent):
    event.page.drawer.open = True

def select_drawer_index(event: ft.ControlEvent, index: int):
    event.page.drawer.selected_index = index

def get_controls_from_current_drawer_index(event: ft.ControlEvent):
    drawer_index = event.page.drawer.selected_index
    module = state.get_current_module()
    module_sections = module.sections
    print(module_sections)
    return module_sections[drawer_index].content

def close_drawer(event: ft.ControlEvent):
    event.page.drawer.open = False

def update_page(event: ft.ControlEvent):
    event.page.update()