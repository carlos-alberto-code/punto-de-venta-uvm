import flet as ft
from typing import Dict, Any, Union

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

        page.window.maximized = True
        page.window.frameless = True
        page.padding = 0

        self.appbar: ft.CupertinoAppBar = ft.CupertinoAppBar(
            automatically_imply_leading=False,
            automatically_imply_middle=False,
            middle=ft.Text('Home'),
            trailing=ft.PopupMenuButton(
                icon=ft.icons.PERSON,
                items=[
                    ft.PopupMenuItem(
                        text='Perfil de usuario',
                        icon=ft.icons.PERSON,
                    ),
                    ft.PopupMenuItem(
                        text='Cambiar tema',
                        icon=ft.icons.CHANGE_CIRCLE,
                        on_click=change_theme,
                    ),
                    ft.PopupMenuItem(
                        text='Configuración',
                        icon=ft.icons.SETTINGS,
                    ),
                    ft.PopupMenuItem(
                        text='Cerrar sesión',
                        icon=ft.icons.LOGOUT,
                        on_click=self._handler_logout,
                    ),
                ]
            )
        )

        self.rail = ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    label=module.name,
                    icon=module.icon,
                ) for module in self._user_modules
            ],
            col=1.10,
            group_alignment=0.0,
            selected_index=0,
            on_change=self._handler_on_change,
        )
        self.shape = ft.ResponsiveRow(
            controls=[
                self.rail,
                HomeContent(user=self._user['username']),
            ],
            col=12,
            expand=True,
        )
        self.controls = [
            self.shape,
        ]
    
    def _handler_on_change(self, event: ft.ControlEvent):
        index: int = event.control.selected_index
        for i, module in enumerate(self._user_modules):
            if i == index:
                self._change_appbar_title(module.name)
                self._update_content(module)
                break
    
    def _handler_logout(self, event: ft.ControlEvent):
        event.page.window.close()
    
    def _change_appbar_title(self, title: str) -> None:
        if self.appbar:
            self.appbar.middle = ft.Text(title)
            self.appbar.update()

    def _update_content(self, module: Module) -> None:
        self.shape.controls[1] = module.content
        self.shape.update()
