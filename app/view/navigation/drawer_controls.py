from typing import List
import flet as ft


class DrawerControls:

    @classmethod
    def top_controls(cls) -> List[ft.Control]:
        return [
            ft.Container(height=14),
            ft.NavigationDrawerDestination(label='Carlos Alberto', icon=ft.icons.VERIFIED),
            ft.Divider(),
        ]
    
    @classmethod
    def middle_controls(cls, drawer_destinations: List[ft.NavigationDrawerDestination]) -> List[ft.Control]:
        return [*drawer_destinations]
    
    @classmethod
    def bottom_controls(cls) -> List[ft.Control]:
        return [
            ft.Divider(),
            ft.NavigationDrawerDestination(label='Configuración', icon=ft.icons.SETTINGS),
            ft.NavigationDrawerDestination(label='Cerrar sesión', icon=ft.icons.EXIT_TO_APP)
        ]
