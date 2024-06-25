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
        self._modules = Module.repo
        self._user_modules = [
            module for module_name, module 
            in self._modules.items() 
            if module_name in self._user['modules']
        ]
        self.current_index: Optional[int] = None

        page.window.maximized = True
        page.window.frameless = True
        page.padding = 0

        self.appbar = ft.AppBar(
            title=ft.Text('Inicio'),
            center_title=True,
            automatically_imply_leading=False,
            toolbar_height=70,
            actions=[
                ft.PopupMenuButton(
                    icon=ft.icons.PERSON,
                    items=[
                        ft.PopupMenuItem(
                            text='Perfil de usuario',
                            icon='person'
                        ),
                        ft.PopupMenuItem(
                            text='Cambiar tema',
                            icon='dark_mode',
                            on_click=change_theme
                        ),
                        ft.PopupMenuItem(
                            text='Configuración',
                            icon='settings'
                        ),
                        ft.PopupMenuItem(
                            text='Cerrar sesión',
                            icon='logout',
                            on_click=lambda e: page.window.close()
                        ),
                    ]
                ),
                ft.Container(width=15),
            ]
        )

        self.rail = ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    label=module.name,
                    icon=module.icon,
                    padding=10,
                ) for module in self._user_modules
            ],
            col=1.10,
            group_alignment=0.0,
            selected_index=0,
            on_change=self.handler_on_change,
        )
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
                    self.content_page = module.content
                    self.controls = [self.update_view(module.content)]
                    self.change_appbar_title(module.name)
                    self.update()
                    break
    
    def change_appbar_title(self, title: str):
        self.appbar.title = ft.Text(title) # type: ignore

    def update_view(self, content: ft.Container) -> ft.ResponsiveRow:
        content.col = 10.90
        return ft.ResponsiveRow(
            controls=[
                self.rail,
                content,
            ],
            col=12,
            expand=True,
        )
