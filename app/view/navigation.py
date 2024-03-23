from typing import List
import flet as ft

from .modules.modules_declaration import create_modules


class _DrawerControls:

    @staticmethod
    def get_top_controls() -> List[ft.Control]:
        return [
            ft.Container(height=14),
            ft.NavigationDrawerDestination(label='Carlos Alberto', icon=ft.icons.VERIFIED_USER),
            ft.Divider()
        ]
    
    @staticmethod
    def get_middle_controls(section_controls: List[ft.NavigationDrawerDestination]) -> List[ft.Control]:
        return [*section_controls]

    @staticmethod
    def get_bottom_controls() -> List[ft.Control]:
        return [
            ft.Divider(),
            ft.NavigationDrawerDestination(label='Configuración', icon=ft.icons.SETTINGS),
            ft.NavigationDrawerDestination(label='Cerrar sesión', icon=ft.icons.EXIT_TO_APP),
        ]


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
    sections = _get_and_build_sections(module)
    _drawer.controls = [
        *_DrawerControls.get_top_controls(),
        *_DrawerControls.get_middle_controls(sections),
        *_DrawerControls.get_bottom_controls(),
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
    sections = _get_and_build_sections(module)
    _drawer.controls = [
        *_DrawerControls.get_top_controls(),
        *_DrawerControls.get_middle_controls(sections),
        *_DrawerControls.get_bottom_controls(),
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
Si aparece cómo título en el Appbar 'Aplicación', significa que no hay secciones en el Drawer.
Eso no debería pasar, porque el primer módulo debería ser seleccionado por defecto junto 
con la primer sección del Drawer para mostrar contenido.

Otro problema es que, al navegar entre módulos, el Drawer mantiene como selección el control anterior.
Esto no debería pasar, porque al cambiar de módulo, el Drawer debería seleccionar el primer control.

Para ello debemos hacer:
- Que el Drawer seleccione el primer control (perteneciente al módulos) al cambiar de módulo.
- Que el Drawer se inicialice con el primer módulo seleccionado y su primer control activo.

Una mejora adicional para mejorar la retroalimentación para el usuario sobre en qué módulo se encuentra
es cambiar el color de fondo del Drawer y el Appbar para que coincidan con el color del módulo seleccionado.
Eso implicaría que cada módulo tenga un color de fondo asociado y relacionado con todos los componentes 
de navegación. Por ahora esa mejora no es prioritaria, pero es algo a tener en cuenta para mejorar la UX.
"""