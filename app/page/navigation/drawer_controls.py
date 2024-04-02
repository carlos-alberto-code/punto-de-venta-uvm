from typing import Optional, List
import flet as ft

class DrawerControls:

    @classmethod
    def _top_controls(cls) -> List[ft.Control]:
        return [
            ft.Container(height=14),
            ft.NavigationDrawerDestination(label='Carlos Alberto', icon=ft.icons.VERIFIED),
            ft.Divider(),
        ]
    
    @classmethod
    def _bottom_controls(cls) -> List[ft.Control]:
        return [
            ft.Divider(),
            ft.NavigationDrawerDestination(label='Configuración', icon=ft.icons.SETTINGS),
            ft.NavigationDrawerDestination(label='Cerrar sesión', icon=ft.icons.EXIT_TO_APP)
        ]
    
    @classmethod
    def load_controls(cls, middle_controls: Optional[List[ft.Control]] = None) -> List[ft.Control]:
        if middle_controls is None:
            middle_controls = []
        return [
        *cls._top_controls(),
        *middle_controls,
        *cls._bottom_controls()
        ]
