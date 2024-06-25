import flet as ft
from typing import Dict, Any, Optional, Union

from modules.modules      import Module
from modules.home_content import HomeContent
from theme.change_theme   import change_theme


class AppView(ft.View):

    def __init__(self, page: ft.Page, user: Union[Dict[str, Any], str]):
        super().__init__()
        self.route: str = 'app/'
        self._user = user if isinstance(user, dict) else {}
        if not self._user:
            raise ValueError('No existe un usuario para mostrar la vista.')
        self._user_modules = [
            module for module_name, module 
            in Module.repo.items() 
            if module_name in self._user['modules']
        ]
        self.current_index: Optional[int] = None

        page.window.maximized = True
        page.window.frameless = True
        page.padding = 0

        self.appbar = self.create_appbar()
        self.rail = self.create_rail()
        self.content_page = HomeContent(user=self._user['username'])

        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    self.rail,
                    self.content_page
                ],
                col=12,
                expand=True,
            )
        ]
    
    def handler_on_change(self, event: ft.ControlEvent):
        index: int = event.control.selected_index
        if index != self.current_index:
            self.current_index = index
            for i, module in enumerate(self._user_modules):
                if i == index:
                    self.update_view(module)
                    break
    
    def handler_logout(self, event: ft.ControlEvent):
        event.page.window.close()
    
    def create_appbar(self, title: str = 'Inicio'):
        return ft.AppBar(
            title=ft.Text(f'{title}'),
            center_title=True,
            automatically_imply_leading=False,
            toolbar_height=70,
            actions=[
                ft.PopupMenuButton(
                    icon=ft.icons.PERSON,
                    items=[
                        ft.PopupMenuItem(text='Perfil de usuario', icon='person'),
                        ft.PopupMenuItem(text='Cambiar tema', icon='dark_mode', on_click=change_theme),
                        ft.PopupMenuItem(text='Configuración', icon='settings'),
                        ft.PopupMenuItem(text='Cerrar sesión', icon='logout', on_click=self.handler_logout),
                    ]
                ),
                ft.Container(width=15),
            ]
        )
    
    def create_rail(self) -> ft.NavigationRail:
        return ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    label=module.name,
                    icon=module.icon,
                ) for module in self._user_modules
            ],
            col=1.10,
            group_alignment=0.0,
            selected_index=0,
            on_change=self.handler_on_change,
        )

    def update_view(self, module: Module) -> None:
        self.appbar = self.create_appbar(module.name)
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    self.rail,
                    module.content
                ],
                col=12,
                expand=True,
            )
        ]
        self.update()
