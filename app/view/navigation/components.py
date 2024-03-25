from typing import List
import flet as ft


class NavigationComponents:

    @classmethod
    def appbar(cls, central_controls: List[ft.Control], action_controls: List[ft.Control]):
        return ft.AppBar(
            title=ft.Row(controls=central_controls),
            center_title=True,
            actions=action_controls,
        )

    @classmethod
    def drawer(cls):
        return ft.NavigationDrawer(
            controls=[],
            selected_index=0,
            open=False
        )

    @classmethod
    def navbar(cls):
        return ft.NavigationBar(
            selected_index=0,
            destinations=[]
        )