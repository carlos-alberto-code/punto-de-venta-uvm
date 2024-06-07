import flet as ft
from typing import List, Optional


class Section(ft.NavigationDrawerDestination):
    """
    This class represents a section (``flet.control``) in the navigation drawer.
    """
    
    def __init__(
            self,
            label: str = 'Not section defined.',
            icon: str = ft.icons.QUERY_BUILDER,
            content: Optional[ft.Control] = None
    ) -> None:
        super().__init__(label, icon)
        if content is None:
            content = ft.Column(
                # alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft.Text('Not controls defined.')]
            )
        self._content = content
    
    @property
    def content(self) -> ft.Control:
        """
        Get the content of the section. The content is the view that will be displayed when the section is selected.
        """
        return self._content


class Module(ft.NavigationDestination):
    """
    This class represents a module in the navigation.
    """

    all_modules: List['Module'] = []

    def __init__(self, label: str, icon: str, *sections: Section) -> None:
        super().__init__(label, icon)
        if not sections:
            sections = (
                Section(),
                Section(),
                Section(),
            )
        self._drawer_sections = sections
        self.all_modules.append(self)
    
    @property
    def drawer_sections(self) -> tuple:
        """
        Get the sections of the drawer.
        """
        return self._drawer_sections
    
    def __repr__(self) -> str:
        """
        Get a string representation of the module.
        """
        return f'Module(label={self.label}, icon={self.icon}, sections={self._drawer_sections})'
    