"""
En este módulo (módulo de Python, no interface) creamos una estructura de datos
para organizar los módulos y secciones que se relacionan a la hora de navegar en
la aplicación. La estructura de datos es la siguiente:

Un Rail es un ``ft.NavigationDestinatio`` que contiene una lista de secciones (Section)
asociadas (``List[Section]``). Cada Section es un ``ft.NavigationDrawerDestination``
que será la forma en la que nos moveremos en las secciones del módulo.
"""

from typing import List
import flet as ft


class Section(ft.UserControl):
    
    def __init__(self, name: str, icon: str, rail: 'Rail') -> None:
        super().__init__()
        self._name = name
        self._icon = icon
        self._rail = rail
        self._rail._add_section(self)

    def __repr__(self):
        return f'Section(name={self._name}, icon={self._icon})'
    
    def build(self) -> ft.NavigationDrawerDestination:
        return ft.NavigationDrawerDestination(
            label=self._name,
            icon=self._icon,
        )


class Rail(ft.UserControl):

    def __init__(self, name: str, icon: str) -> None:
        super().__init__()
        self._name = name
        self._icon = icon
        self._sections: List[Section] = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def sections(self) -> List[Section]:
        return self._sections

    @sections.setter
    def sections(self, sections: List[Section]) -> None:
        self._sections = sections
    
    def _add_section(self, section: Section) -> None:
        self._sections.append(section)
    
    def build(self) -> ft.NavigationDestination:
        return ft.NavigationDestination(
            label=self._name,
            icon=self._icon,
        )
