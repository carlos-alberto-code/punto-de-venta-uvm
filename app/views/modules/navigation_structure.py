"""
Este archivo contiene las clases que representan la estructura de navegación de la aplicación.
Un ``Rail`` es un ``ft.NavigationDestination`` que se usará para representar el módulo en el ``ft.NavigationBar``.
Una ``Section`` es un ``ft.NavigationDrawerDestination`` que se usará para representar una sección del módulo en el ``ft.NavigationDrawer``.
Estos dos elementos deben relacionarse de algún modo para que a la hora de desplazarnos entre los módulos
podamos tener opciones pertenecientes a los objetivos de cada módulo. Para ello se ha creado el ``Module``.

Un ``Module`` es una estructura que nos permitirá relacionar un ``Rail`` con determinadas ``Sections``.
Existirán tantas instanicas de ``Module`` como módulos tenga la aplicación.

Prácticas recomendadas:

Nuestro flujo de trabajo actual se trata de que cada uno codifique un módulo de la aplicación.
Para ello, cada uno de los módulos debe ser creado en un archivo o carpeta separada.
Asi será claro que cada uno de los módulos es independiente y no depende de los demás.

Al final, todos los módulos deben ser importados en el archivo ``app/views/modules/create_modules.py``.
De forma que en el archivo ``app/main.py`` se llame a la función ``create_modules`` que se encargará de crear
todos los módulos de la aplicación.
"""

from typing import List
import flet as ft


class Section(ft.UserControl):
    
    def __init__(self, name: str, icon: str) -> None:
        super().__init__()
        self._name = name
        self._icon = icon
    
    @property
    def name(self) -> str:
        return self._name
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name})'
    
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
    
    
    def build(self) -> ft.NavigationDestination:
        return ft.NavigationDestination(
            label=self._name,
            icon=self._icon,
        )


class Module:
    
    def __init__(self, name: str, icon: str, *sections: Section) -> None:
        self._name = name
        self._rail = Rail(name, icon)
        self._sections = list(sections)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def rail(self) -> Rail:
        return self._rail
    
    @property
    def sections(self) -> List[Section]:
        return self._sections
    
    def __repr__(self) -> str:
        return f'Module(name={self.name}, sections={self._sections})'
