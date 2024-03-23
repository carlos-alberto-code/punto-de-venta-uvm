from typing import List
import flet as ft

from .modules.modules_declaration import create_modules


class _DrawerControls:

    @staticmethod
    def get_top_controls() -> List[ft.Control]:
        return [
            ft.Container(height=14),
            ft.NavigationDrawerDestination(label='Carlos Alberto', icon=ft.icons.CIRCLE),
            ft.Divider()
        ]
    
    @staticmethod
    def get_middle_controls(
        section_controls: List[ft.NavigationDrawerDestination]
    ) -> List[ft.NavigationDrawerDestination]:
        return section_controls

    @staticmethod
    def get_bottom_controls() -> List[ft.Control]:
        return [
            ft.Divider(),
            ft.NavigationDrawerDestination(label='Configuración', icon=ft.icons.SETTINGS),
            ft.NavigationDrawerDestination(label='Cerrar sesión', icon=ft.icons.EXIT_TO_APP),
        ]


# EVENT HANDLER

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


# Implementation


_modules = create_modules()
_navbar = ft.NavigationBar(
    destinations=_get_and_build_destinations(),
    on_change=_update,
)
_drawer = ft.NavigationDrawer(controls=[])
_appbar = ft.AppBar(
    title=ft.Text('Aplicación', size=20),
    actions=[
        ft.IconButton(icon=ft.icons.DARK_MODE),
        ft.IconButton(icon=ft.icons.NOTIFICATIONS),
        ft.IconButton(icon=ft.icons.CLOSE),
    ]
)

# Export

def active_navs():
    return _navbar, _drawer, _appbar