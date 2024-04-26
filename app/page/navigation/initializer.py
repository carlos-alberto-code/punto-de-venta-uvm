from .module import Module


class Initializer:
    """
    Se encarga de configurar las cosas para que la aplicación renderice el módulo inicial.
    """
    def __init__(self, modules: list[Module], navbar_index: int = None, drawer_index: int = 0) -> None:
        self._modules = modules
        self._navbar_index = navbar_index
        self._drawer_index = drawer_index
