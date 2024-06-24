import flet as ft
from typing import Optional

from users.user  import User
from naveasey.naveasey      import Module
from modules.home_content           import HomeContent
from theme.change_theme     import change_theme


class AppView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.__screen = page
        self.route: str = 'app/'
        self.__user: Optional[User] = None
        
    
    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user: User):
        self.__user = user
        self.build_view()
        
    def build_view(self):
        if self.__user:
            if self.__user.theme_mode == ft.ThemeMode.LIGHT:
                self.__screen.theme_mode = ft.ThemeMode.LIGHT
                # TODO: Lógica para cambiar el tema a claro
            if self.__user.theme_mode == ft.ThemeMode.DARK:
                self.__screen.theme_mode = ft.ThemeMode.DARK
                # TODO: Lógica para cambiar el tema a oscuro
            
            self.__set_page_config()
            self.__appbar = self.__create_appbar()
            self.__screen.appbar = self.__appbar
            self.rail = self.__create_navigation_rail(self.__user.modules)
            self.shape = self.__create_shape(rail=self.rail, home_content=HomeContent(user=self.__user.username), user=self.__user)
            self.__screen.add(self.shape)
            
    def __set_page_config(self):
        self.__screen.window.maximized = True
        self.__screen.window.frameless = True
        self.__screen.padding = 0
        self.__screen.clean()
    
    def __create_appbar(self):
        return ft.AppBar(
            center_title=True,
            actions=[
                ft.IconButton(icon='dark_mode', tooltip='Cambiar tema', on_click=change_theme),
                ft.PopupMenuButton(
                    icon=ft.icons.MORE_VERT,
                    items=[
                        ft.PopupMenuItem(text='Perfil de usuario', icon='person'),
                        ft.PopupMenuItem(text='Configuración', icon='settings'),
                        ft.PopupMenuItem(text='Cerrar sesión', icon='logout', on_click=lambda e: self.__screen.window.close()),
                    ]
                )
            ]
        )

    def __create_navigation_rail(self, modules: list[Module]):
        return ft.NavigationRail(
            col=1.20,
            elevation=30,
            group_alignment=-1,
            destinations=[*modules],
            on_change=self.handle_on_change,
        )
    
    def __create_shape(self, rail: ft.NavigationRail, home_content: HomeContent, user: User):
        return ft.ResponsiveRow(
            controls=[
                rail,
                HomeContent(user=user.username),
            ],
            expand=True,
            col=12,
        )
    
    def handle_on_change(self, event: ft.ControlEvent):
        index = event.control.selected_index
        if self.user:
            modules = self.user.modules
            for i, module in enumerate(modules):
                if i == index:
                    self.shape.controls[1] = module.content
                    self.shape.update()
                    self.__appbar.title = ft.Text(module.name)
                    self.__appbar.update()
                    break
