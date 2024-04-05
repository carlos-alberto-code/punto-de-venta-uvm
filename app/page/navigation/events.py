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


def update_content(event: ft.ControlEvent):
    module = state.get_current_module()
    sections = module.sections
    drawer_index = get_drawer_index(event)
    section = sections[drawer_index]
    clean_page(event)
    event.page.add(section.content)
    close_drawer(event) # TODO: Algo pasa que el drawer no se cierra aquí, pero sí en el otro evento
    update_page(event)



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
    return module_sections[drawer_index].content

def close_drawer(event: ft.ControlEvent):
    event.page.drawer.open = False

def update_page(event: ft.ControlEvent):
    event.page.update()

def get_drawer_index(event: ft.ControlEvent) -> int:
    return event.page.drawer.selected_index