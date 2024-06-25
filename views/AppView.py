import flet as ft
from typing import Dict, Any, Union

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

        page.window.maximized = True
        page.window.frameless = True
        page.padding = 0

        self.appbar = ft.AppBar(
            title=ft.Text('Inicio'),
            center_title=True,
            elevation=30,
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
                ft.Container(width=20),
            ]
        )

        self.rail = ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    icon=module.icon,
                    selected_icon=module.selected_icon,
                    label=module.name,
                ) for module in self._user_modules
            ],
            on_change=self.handler_on_change,

        )
        self.controls = [
        ]
    
    def handler_on_change(self, event: ft.ControlEvent):
        index: int = event.control.selected_index
        for i, module in enumerate(self._user_modules):
            if i == index:
                self.controls = [module.content]
                self.change_appbar_title(module.name)
                self.update()
                break
    
    def change_appbar_title(self, title: str):
        self.appbar.title = ft.Text(title) # type: ignore
        

    
    # def build_view(self):
            
    #         self.__appbar = self.__create_appbar()
    #         self.__screen.appbar = self.__appbar
    #         self.rail = self.__create_navigation_rail(self.__user.modules)
    #         self.shape = self.__create_shape(rail=self.rail, home_content=HomeContent(user=self.__user.username), user=self.__user)
    #         self.__screen.add(self.shape)
            
        
    
    # def __create_appbar(self):
    #     return ft.AppBar(
    #         center_title=True,
    #         actions=[
    #             ft.IconButton(icon='dark_mode', tooltip='Cambiar tema', on_click=change_theme),
    #             ft.PopupMenuButton(
    #                 icon=ft.icons.MORE_VERT,
    #                 items=[
    #                     ft.PopupMenuItem(text='Perfil de usuario', icon='person'),
    #                     ft.PopupMenuItem(text='Configuración', icon='settings'),
    #                     ft.PopupMenuItem(text='Cerrar sesión', icon='logout', on_click=lambda e: self.__screen.window.close()),
    #                 ]
    #             )
    #         ]
    #     )

    # def __create_navigation_rail(self, modules: list[Module]):
    #     return ft.NavigationRail(
    #         col=1.20,
    #         elevation=30,
    #         group_alignment=-1,
    #         destinations=[*modules],
    #         on_change=self.handle_on_change,
    #     )
    
    # def __create_shape(self, rail: ft.NavigationRail, home_content: HomeContent, user: Dict[str, Any]):
    #     return ft.ResponsiveRow(
    #         controls=[
    #             rail,
    #             HomeContent(user=user.username),
    #         ],
    #         expand=True,
    #         col=12,
    #     )
    
    # def handle_on_change(self, event: ft.ControlEvent):
    #     index = event.control.selected_index
    #     if self.__user:
    #         modules = self.__user.modules
    #         for i, module in enumerate(modules):
    #             if i == index:
    #                 self.shape.controls[1] = module.content
    #                 self.shape.update()
    #                 self.__appbar.title = ft.Text(module.name)
    #                 self.__appbar.update()
    #                 break
