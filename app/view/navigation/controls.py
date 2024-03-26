from typing import List
import flet as ft


class AppbarControls:

    @classmethod
    def central_controls(cls, title: str) -> ft.Row:
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=ft.icons.KEYBOARD_DOUBLE_ARROW_LEFT),
                ft.Text(f'{title}'),
                ft.IconButton(icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT),
            ]
        )

    @classmethod
    def action_controls(cls) -> List[ft.Control]:
        return [
            ft.IconButton(icon=ft.icons.DARK_MODE),
            ft.IconButton(icon=ft.icons.LIGHT_MODE),
            ft.IconButton(icon=ft.icons.CLOSE),
        ]


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
