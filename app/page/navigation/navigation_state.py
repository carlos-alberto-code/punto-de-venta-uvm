from .builder import Module


class NavigationStateManager:
    """
    Esta clase tiene la responsabilidad de gestionar el estado de la navegación de la aplicación.
    
    """
    def __init__(self) -> None:
        self._current_index_module = 0

    @property
    def current_index(self):
        return self._current_index_module

    def get_module_from_destination_index(self, index: int):
        self._current_index_module = index
        return Module.all_modules[index]

    def get_current_module(self):
        return Module.all_modules[self._current_index_module]
    
    # función para obtener los controles de los módulos
    def get_navigation_bar_controls(self):
        return [module.rail.build() for module in Module.all_modules]
