# Aquí se maneja la lógica de los eventos de los diferentes componentes de la vista de la compra
# Además se sigue un principio que es es cada componente se modifica en su contexto.
import flet as ft
from controllers.controllers import ProductController
from purchase_view.ProductCard import ProductCard


product_controller = ProductController() # Controlador de productos

# Eventos de la barra de búsqueda

def handle_on_tap(event: ft.ControlEvent):
    searcher.close_view()
    gird_view.controls = _create_product_cards(product_controller.get_all())
    gird_view.update()
    

def handle_on_change(event: ft.ControlEvent):
    results = product_controller.search(str(searcher.value))
    gird_view.controls = _create_product_cards(results)
    gird_view.update()

def _create_product_cards(results: list) -> list[ft.Card]:
    return [
        ProductCard(
            product_description=product.unit + ' ' + product.category + ' ' + product.brand,
            existences=product.quantity
        ) for product in results
    ]


searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handle_on_tap,
    on_change=handle_on_change
)


gird_view = ft.GridView( # Vista de productos
    controls=[
        *_create_product_cards(product_controller.get_all())
    ],
    expand=1,
    runs_count=3,
    max_extent=420,
    child_aspect_ratio=5.5,
    spacing=5,
    run_spacing=5,
)
