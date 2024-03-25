from typing import List
import flet as ft


from .modules.modules_declaration import create_modules # Creación de módulos
from .navigation.drawer_controls import DrawerControls # DrawerControls


drawer_controls = DrawerControls


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


_modules = create_modules()
_navbar = ft.NavigationBar(
    selected_index=SELECTED_MODULE,
    destinations=_get_and_build_destinations(),
    on_change=_update,
)
_drawer = ft.NavigationDrawer(controls=[], selected_index=0, open=False)
_appbar = ft.AppBar(
    title=ft.Text('Aplicación'),
    center_title=True,
    actions=[
        ft.IconButton(icon=ft.icons.DARK_MODE),
        ft.IconButton(icon=ft.icons.NOTIFICATIONS),
        ft.IconButton(icon=ft.icons.CLOSE),
    ]
)
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