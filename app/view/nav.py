from typing import List
import flet as ft


from .modules.modules_declaration import all_modules # Creación de módulos
from .navigation.controls.drawer_controls import DrawerControls # DrawerControls
from .navigation.controls.appbar_controls import AppbarControls # AppbarControls
from .navigation.navigation_components import NavigationComponents # NavigationComponents


# EVENT HANDLER
    
SELECTED_MODULE = 0
SELECTED_SECTION = 1

# Principal functions
    
def _update(event):
    index = event.control.selected_index
    module = _get_module(index)
    _update_drawer_sections(module)
    _update_appbar(module)
    

def _update_drawer_sections(module):
    drawer_destinations = _get_and_build_sections(module)
    _drawer.controls = [
        *drawer_controls.top_controls(),
        *drawer_controls.middle_controls(drawer_destinations),
        *drawer_controls.bottom_controls()
    ]
    _drawer.selected_index = SELECTED_SECTION
    _drawer.open = True
    _drawer.update()


def _update_appbar(module):
    _appbar.title = ft.Text(module.name)
    _appbar.update()


# Secondary functions
    
def _get_and_build_destinations() -> List[ft.NavigationDestination]:
    return [module.rail.build() for module in _modules]


def _get_module(index: int):
    return _modules[index]


def _get_and_build_sections(module) -> List[ft.NavigationDrawerDestination]:
    return [section.build() for section in module.sections]


# Initial functions

def _init_drawer():
    module = _get_module(SELECTED_MODULE) # Módulo seleccionado por defecto
    drawer_destinations = _get_and_build_sections(module)
    _drawer.controls = [
        *drawer_controls.top_controls(),
        *drawer_controls.middle_controls(drawer_destinations),
        *drawer_controls.bottom_controls(),
    ]
    _drawer.selected_index = SELECTED_SECTION
    _drawer.open = True
    _appbar.title = ft.Text(module.name)


# Implementation


appbar_controls = AppbarControls
drawer_controls = DrawerControls
nav_components = NavigationComponents

_modules = all_modules

_appbar = nav_components.appbar(
    central_controls=appbar_controls.central_controls(title="App"),
    action_controls=appbar_controls.action_controls()
)
_drawer = nav_components.drawer()
_navbar = nav_components.navbar()

_init_drawer()

# Export

def active_navs():
    return _navbar, _drawer, _appbar



# TODO: Fix the following issues:
"""

TODO: Se debe mejorar el código, hay que hacerlo más limpio.

Una mejora adicional para mejorar la retroalimentación para el usuario sobre en qué módulo se encuentra
es cambiar el color de fondo del Drawer y el Appbar para que coincidan con el color del módulo seleccionado.
Eso implicaría que cada módulo tenga un color de fondo asociado y relacionado con todos los componentes 
de navegación. Por ahora esa mejora no es prioritaria, pero es algo a tener en cuenta para mejorar la UX.

Otra opción para hacer lo anterior es simplemente mostrar títulos entre las secciones del Drawer, el título
en el drawer debe coincidir con el del módulo y por tanto el del appbar.
"""