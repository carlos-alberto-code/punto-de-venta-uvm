from typing import List
import flet as ft


class AppbarControls:

    @classmethod
    def central_controls(cls, title: str) -> List[ft.Control]:
        return [
            ft.IconButton(icon=ft.icons.ARROW_LEFT),
            ft.Text(f'{title}'),
            ft.IconButton(icon=ft.icons.ARROW_RIGHT),
        ]

    @classmethod
    def action_controls(cls) -> List[ft.Control]:
        return [
            ft.IconButton(icon=ft.icons.DARK_MODE),
            ft.IconButton(icon=ft.icons.LIGHT_MODE),
            ft.IconButton(icon=ft.icons.CLOSE),
        ]