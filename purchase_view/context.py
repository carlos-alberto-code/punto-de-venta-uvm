# Aquí se maneja la lógica de los eventos de los diferentes componentes de la vista de la compra
# Además se sigue un principio que es es cada componente se modifica en su contexto.
import flet as ft
from controllers.controllers import ProductController


# Buscador de productos y sus eventos

def handle_on_tap(event: ft.ControlEvent):
    searcher.close_view()

def handle_on_change(event: ft.ControlEvent):
    print('\n', '-'*10, 'Resultados', '-'*10, '\n')
    r = product_controller.search(str(searcher.value))
    print(r)

product_controller = ProductController()

searcher = ft.SearchBar(
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handle_on_tap,
    on_change=handle_on_change
)

# product_table = 