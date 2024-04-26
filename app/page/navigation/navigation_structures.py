import flet as ft

from .navigation_state_manager import NavigationStateManager
from .on_change_events import update_module, update_content
from .initializer import Initializer


class NavigationStructureFactory:

    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance


    def __init__(self, initializer: Initializer) -> None:
        self.init               = initializer

        # Inyectamos los valores iniciales para el estado de la navegación.
        self.state              = NavigationStateManager()
        self.state.navbar_index = self.init.navbar_index 
        self.state.drawer_index = self.init.drawer_index
        self.state.modules      = self.init.modules

        self.init_module        = self.init.initial_module # Módulo inicial.
    
    def appbar(self, appbar_actions: list[ft.Control] = []):
        return ft.AppBar(
            center_title=True,
            title=ft.Text(f'{self.init_module.label}'),
            actions=appbar_actions
        )
    
    @property
    def navbar(self):
        return ft.NavigationBar(
            selected_index=self.init.navbar_index,
            destinations=[module for module in self.init.modules],
            on_change=update_module
        )
    
    @property
    def drawer(self):
        return ft.NavigationDrawer(
            open=True,
            selected_index=self.init.drawer_index,
            controls=[section for section in self.init_module.drawer_sections],
            on_change=update_content
        )