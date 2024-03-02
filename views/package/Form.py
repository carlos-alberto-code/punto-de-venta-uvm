'''
Consideraciones del algoritmo:
- Se debe detectar la fila más grande y tomar el número
- Detectar la longitud de cada fila y rellenar los espacios con un objeto y buscar que el control se expanda

Otro algoritmo se encarga de:
- que a la hora de insertar una nueva fila en una determinada posición, se actualicen los índices
del árbol correctamente.
'''
import flet as ft


mtx = {
    0: ft.Row(expand=True),
    1: ft.Row(),
    2: ft.Row(),
}

matriz = [
    ft.Row,
    [4, 5, 6, ''],
    [7, 8, 9, 10]
]
from typing import Optional


class Form:

    def __init__(
            self,
            title: Optional[str] = None,
            color_palette: Optional[ft.Theme] = None
            con
    ) -> None:
        # Características del formulario
        self.title = title
        self.color_palette = color_palette
        self.control_matrix: dict[int, ft.Row] = {}

    def __getitem__(self, index):
        return self.tree[index]
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'

print(Form())

class LoggingView(Form):
    pass

print(LoggingView())

class Asub(LoggingView):
    pass

print(Asub())

