from .module import Module

from abc import ABC, abstractmethod
from typing import List
import flet as ft


class Observer(ABC):
    """
    Clase abstracta que sirve como interfaz para los observadores.
    Los observadores son los componentes que se actualizan cuando el sujeto cambia.
    En nuestro caso el sujeto es el Navbar y el observador es el componente Drawer.
    """
    @abstractmethod
    def update(self, sections: List[ft.NavigationDrawerDestination]):
        """Cada observador implementa este método, pero cada uno implementa su propia lógica"""
        pass

class Subject(ABC):
    """
    Clase abstracta que sirve como interfaz para los sujetos.
    Los sujetos son los componentes que pueden ser observados.
    En nuestro caso el sujeto es el Navbar y el observador es el componente Drawer.
    """

    @abstractmethod
    def register(self, observer: Observer):
        """Agrega un observador a la lista de observadores"""
        pass

    @abstractmethod
    def unregister(self, observer: Observer):
        """Elimina un observador de la lista de observadores"""
        pass

    @abstractmethod
    def notify(self):
        """Notifica a todos los observadores que el sujeto ha cambiado"""
        pass


class Drawer(Observer, ft.UserControl):

    def __init__(self):
        super().__init__()
        self.drawer = ft.NavigationDrawer()
        self.top_controls = [
            ft.Container(height=14),
            ft.NavigationDrawerDestination(
                label='Usuario',
                icon=ft.icons.PERSON,
            ),
            ft.Divider(),
        ]
        self.middle_controls = []
        self.bottom_controls = [
            ft.Divider(),
            ft.NavigationDrawerDestination(
                label='Configuración',
                icon=ft.icons.SETTINGS,
            ),
            ft.NavigationDrawerDestination(
                label='Cerrar sesión',
                icon=ft.icons.LOGOUT,
            ),
        ]
    
    def update(self, sections: List[ft.NavigationDrawerDestination]): # List[ft.NavigationDrawerDestination]
        self.drawer.controls = [
            *self.top_controls,
            *sections,
            *self.bottom_controls,
        ]
        self.drawer.open = True
        self.drawer.update()
    
    def build(self):
        return self.drawer
    

class Navbar(Subject, ft.UserControl):

    def __init__(self, modules: List[Module]):
        super().__init__()
        self.observers: List[Observer] = []
        self.modules: List[Module] = modules
        self.destinations: List[ft.NavigationDestination] = [
            module.rail.build() for module in self.modules
        ]
        self.sections: List[ft.NavigationDrawerDestination] = []
        self.navbar = ft.NavigationBar(
            destinations=self.destinations,
            on_change=self.find_sections_and_notify
        )

    def register(self, observer: Observer):
        self.observers.append(observer)
        
    def unregister(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.sections)
    
    def find_sections_and_notify(self, event):
        index = event.control.selected_index
        sections = self.modules[index].sections
        self.sections = [section.build() for section in sections]
        self.notify()

    def set_sections(self):
        self.sections = [section.build() for section in self.modules[0].sections]
        self.notify()
        
    
    def build(self):
        return self.navbar


class Appbar(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.appbar = ft.AppBar(
            actions=[
                ft.IconButton(icon=ft.icons.DARK_MODE_OUTLINED),
                ft.IconButton(icon=ft.icons.NOTIFICATIONS),
                ft.IconButton(icon=ft.icons.CLOSE)
            ]
        )
    
    def build(self):
        return self.appbar