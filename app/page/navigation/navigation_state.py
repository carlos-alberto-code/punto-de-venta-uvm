from typing import List

from .module import Module


class NavigationStateManager:
    """
    Esta clase tiene la responsabilidad de gestionar el estado de la navegación de la aplicación.
    Cuando se de un evento de cambio en el ``ft.navigation_bar`` esta clase debe saber el índice
    del ``ft.destination`` que se ha seleccionado y devolver el módulo correspondiente.

    Se tienen setters para poder cambiar la lista de módulos en tiempo de ejecución.
    """

    _instance = None

    def __new__(cls, *args, **kwargs) -> 'NavigationStateManager':
        if not cls._instance:
            cls._instance = super(NavigationStateManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        self._modules: List[Module] = []
        self._current_destination_index = 0

    @property
    def modules(self) -> List[Module]:
        return self._modules
    
    @modules.setter
    def modules(self, modules: List[Module]) -> None:
        self._modules = modules

    @property
    def get_current_destination_index(self) -> int:
        return self._current_destination_index

    @get_current_destination_index.setter
    def set_destination_index(self, index: int) -> None:
        self._current_destination_index = index

    @property
    def current_module(self) -> Module:
        return self._modules[self._current_destination_index]
