from typing import List

import flet as ft

from package_navigation.Module import Module


class Initializer:
    """
    Por ahora, los valores que se definan en el inicializador, serán los valores por defecto
    a lo largo de toda la app, por ejemplo, el indice del drawer se tomará para que en cada cambio
    de módulo, siempre se seleccione la sección que hace referencia a ese indice. Para eso se ha 
    configurado un manejo de excepciones para que haya concordancia en todas las secciones.

    En un futuro podemos establecer valores booleanos para determinar si una sección será la que
    se seleccionará por defecto, esto para cada módulo.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, modules: List[Module], navbar_index: int, drawer_index: int) -> None:
        if not modules:
            raise ValueError('Initializer: modules list is empty.')
        if navbar_index >= len(modules):
            raise ValueError(f'Initializer: navbar_index ({navbar_index}) is out of range for modules list.')
        # Comprobar si el drawer_index está fuera del rango de algún módulo, para lanzar una advertencia.
        for module in modules:
            if drawer_index >= len(module.drawer_sections):
                raise IndexError(f'Initializer: drawer_index ({drawer_index}) is out of range for module "{module.label}". Change it to a valid index for all modules.')
        self._modules = modules
        self._navbar_index = navbar_index
        self._drawer_index = drawer_index
    
    @property
    def modules(self) -> List[Module]:
        return self._modules
    
    @modules.setter
    def modules(self, modules: List[Module]) -> None:
        self._modules = modules
    
    @property
    def navbar_index(self) -> int:
        return self._navbar_index

    @navbar_index.setter
    def navbar_index(self, index: int) -> None:
        self._navbar_index = index
    
    @property
    def drawer_index(self) -> int:
        return self._drawer_index
    
    @drawer_index.setter
    def drawer_index(self, index: int) -> None:
        self._drawer_index = index
    
    @property
    def initial_module(self) -> Module:
        return self.modules[self._navbar_index]
    
    @property
    def initial_drawer_section_content(self) -> ft.Control:
        '''
        Devuelve el contenido de la sección del drawer que se seleccionó en el inicializador.
        '''
        return self.initial_module.drawer_sections[self._drawer_index].content

    def __repr__(self) -> str:
        return (
            f'Initializer(self.NAVBAR_INDEX={self._navbar_index}, self.DRAWER_INDEX={self._drawer_index}) '
            f'-> Has {len(self.modules)} modules'
            f'\nModule names are: {[module.label for module in self.modules]}'
            f'\nThe selected module is "{self.initial_module.label}", and it has {len(self.initial_module._drawer_sections)} sections.'
            f'\nThe section names are: {[section.label for section in self.initial_module._drawer_sections]}'
            f'\n\nEnd Initializer...'
        )
    