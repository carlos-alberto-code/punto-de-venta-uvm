import flet as ft
    

class Section(ft.NavigationDrawerDestination):
    
    def __init__(
            self,
            label: str = 'Not section defined.',
            icon: str = ft.icons.QUERY_BUILDER,
            content: ft.Control = ft.Column(
                # alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft.Text('Not controls defined.')]
            )
    ) -> None:
        super().__init__(label, icon)
        self._content = content
    
    @property
    def content(self) -> ft.Control:
        return self._content


class Module(ft.NavigationDestination):

    all_modules: list['Module'] = []

    def __init__(self, label: str, icon: str, *sections: Section) -> None:
        if not sections:
            sections = (
                Section(),
                Section(),
                Section(),
            )
        super().__init__(label, icon)
        self._drawer_sections = sections
        self.all_modules.append(self)
    
    @property
    def drawer_sections(self):
        return self._drawer_sections
    
    
    def __repr__(self):
        return f'Module(label={self.label}, icon={self.icon}, sections={self._drawer_sections})'
