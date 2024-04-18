from typing import List
import flet as ft


class Rail(ft.NavigationDestination):

    def __init__(self, name: str, icon: str) -> None:
        super().__init__()
        self.label = name
        self.icon = icon
    

class Section(ft.NavigationDrawerDestination):
    
    def __init__(
            self,
            name: str = 'Undefined',
            icon: str = ft.icons.QUERY_BUILDER,
            content: ft.Control = ft.Column(controls=[ft.Text('Not controls defined.')])
    ) -> None:
        super().__init__()
        self.label = name
        self.icon = icon
        self._content = content
    
    @property
    def content(self) -> ft.Control:
        return self._content
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.label})'


class Module:

    all: List['Module'] = []

    def __init__(self, name: str, icon: str, *sections: Section) -> None:
        if not sections:
            sections = (
                Section(),
                Section(),
                Section(),
            )
        self._name = name
        self._rail = Rail(name, icon)
        self._sections = sections
        Module.all.append(self)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def rail(self) -> Rail:
        return self._rail
    
    @property
    def sections(self) -> tuple[Section, ...]:
        return self._sections
    
    def __repr__(self) -> str:
        return f'Module(name={self.name}, sections={self._sections})'
