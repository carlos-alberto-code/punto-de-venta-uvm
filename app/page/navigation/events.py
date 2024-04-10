from .navigation_state import NavigationStateManager

from time import sleep
import flet as ft


navigation_state_manager = NavigationStateManager()


def update_module(event: ft.ControlEvent):
    _clean_page(event)
    navigation_state_manager.set_destination_index = _get_destination_index(event)
    module = navigation_state_manager.current_module
    _update_appbar_title(event, module.name)
    _update_drawer_controls(event, module)
    _open_drawer(event)
    _select_drawer_index(event, 0)
    event.page.add(_get_content_from_current_drawer_destination(event))
    sleep(0.7)
    _close_drawer(event)
    _update_page(event)


def update_content(event: ft.ControlEvent):
    module = navigation_state_manager.current_module
    sections = module.sections
    drawer_index = _get_drawer_index(event)
    section = sections[drawer_index]
    _clean_page(event)
    event.page.add(section.content)
    _close_drawer(event) # TODO: Algo pasa que el drawer no se cierra aquí, pero sí en el otro evento
    _update_page(event)



def _clean_page(event: ft.ControlEvent) -> None:
    event.page.clean()

def _get_destination_index(event: ft.ControlEvent) -> int:
    return event.page.navigation_bar.selected_index

def _update_appbar_title(event: ft.ControlEvent, title: str) -> None:
    event.page.appbar.title = ft.Text(title)

def _update_drawer_controls(event, module):
    event.page.drawer.controls = [control.build() for control in module.sections]

def _open_drawer(event: ft.ControlEvent):
    event.page.drawer.open = True

def _select_drawer_index(event: ft.ControlEvent, index: int):
    event.page.drawer.selected_index = index

def _get_content_from_current_drawer_destination(event: ft.ControlEvent):
    drawer_index = event.page.drawer.selected_index
    module = navigation_state_manager.current_module
    module_sections = module.sections
    return module_sections[drawer_index].content

def _close_drawer(event: ft.ControlEvent):
    event.page.drawer.open = False

def _update_page(event: ft.ControlEvent):
    event.page.update()

def _get_drawer_index(event: ft.ControlEvent) -> int:
    return event.page.drawer.selected_index