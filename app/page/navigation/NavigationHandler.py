# Busco un objeto que me permita manejar el estado de la navegación.
# El evento de cambio de módulo, debe actualizar el módulo seleccionado en el Navbar
# Con este objeto puedo saber en qué módulo estoy actualmente.
# Además, puedo establecer un valor inicial para renderizar los controles del módulo determinado.

from .builder import Module


class State:
    def __init__(self, initial_module: int = 0) -> None:
        self._current_index_module = initial_module

    @property
    def current_index(self):
        return self._current_index_module

    def get_module_from_destination_index(self, index: int):
        self._current_index_module = index
        return Module.all_modules[index]

    def get_current_module(self):
        return Module.all_modules[self._current_index_module]
