from typing import List

from package_navigation.Module import Module


class NavigationStateManager:
    # Tiene la responsabilidad de mantener el estado de la navegación.
    
    _instance = None

    # Implementar un singleton para que el estado de la navegación sea único.
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._modules: list[Module]
        self._drawer_index: int
        self._navbar_index: int
    
    @property
    def modules(self) -> List[Module]:
        return self._modules
    
    @modules.setter
    def modules(self, modules: List[Module]) -> None:
        self._modules = modules
    
    @property
    def drawer_index(self) -> int:
        return self._drawer_index
    
    @drawer_index.setter
    def drawer_index(self, index: int) -> None:
        self._drawer_index = index

    @property
    def navbar_index(self) -> int:
        return self._navbar_index
    
    @navbar_index.setter
    def navbar_index(self, index: int) -> None:
        self._navbar_index = index
    
    @property
    def current_module(self) -> Module:
        return self._modules[self._navbar_index]
    
    def __repr__(self) -> str:
        return f'State(navbar_index={self.navbar_index}, drawer_index={self.drawer_index})'
    