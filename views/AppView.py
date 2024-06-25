import flet as ft
from typing import Dict, Any, Optional, Union

from modules.modules      import Module
from modules.home_content import HomeContent
from theme.change_theme   import change_theme


class AppView(ft.View):

    def __init__(self, page: ft.Page, user: Union[Dict[str, Any], str]):
        super().__init__()
        self.route: str = 'app/'
        self.__user = user if isinstance(user, dict) else {}
        if not self.__user:
            raise ValueError('No existe un usuario para mostrar la vista.')
        self._modules = Module.repo
        self._user_modules = [
            module for module_name, module 
            in self._modules.items() 
            if module.name in self.__user['modules']
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
        self.controls = [self.create_controls(HomeContent(self.__user['username']))]
        
    
    def handler_on_change(self, event: ft.ControlEvent):
        index: int = event.control.selected_index
        if index != self.current_index:
            self.current_index = index
            for i, module in enumerate(self._user_modules):
                print(i, module.name)
                if i == index:
                    self.content_page = module.content
                    self.controls = [self.create_controls(module.content)]
                    self.change_appbar_title(module.name)
                    self.update()
                    break
    
    def change_appbar_title(self, title: str):
        self.appbar.title = ft.Text(title) # type: ignore
    
    def create_rail(self) -> ft.NavigationRail:
        return ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    icon=module.icon,
                    selected_icon=module.selected_icon,
                    label=module.name,
                ) for module in self._user_modules
            ],
            col=1.20,
            on_change=self.handler_on_change,
        )

    def create_controls(self, content: ft.Container) -> ft.ResponsiveRow:
        content.col = 10.80
        return ft.ResponsiveRow(
            controls=[
                self.create_rail(),
                content,
            ],
            col=12,
            expand=True,
        )
