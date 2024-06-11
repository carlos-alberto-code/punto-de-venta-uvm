# Aquí se maneja la lógica de los eventos de los diferentes componentes de la vista de la compra
# Además se sigue un principio que es es cada componente se modifica en su contexto.
import flet as ft
from controllers.controllers import ProductController
from purchase_view.ProductCard import ProductCard
from purchase_view.ProductDTO import ProductDTO as Product # Data Transfer Object


# HANDLERS ---------------------------------------------------------------------

def handle_on_tap(event: ft.ControlEvent): # Evento tap de la barra de búsqueda
    searcher.close_view()
    products = _wrap_productDTO_list(product_controller.get_all())
    gird_view.controls = _create_GirdView_product_cards(products)
    gird_view.update()
    
def handle_on_change(event: ft.ControlEvent): # Evento de búsqueda en tiempo real
    results = product_controller.search(str(searcher.value))
    products = _wrap_productDTO_list(results)
    gird_view.controls = _create_GirdView_product_cards(products)
    gird_view.update()

def handle_on_card_button_click(event: ft.ControlEvent): # Evento de click en el botón de la tarjeta
    button = event.control
    # Transferir los datos del producto seleccionado al formulario de compra


# HELPER FUNCTIONS ------------------------------------------------------------

def _wrap_productDTO_list(results: list) -> list[Product]: # Envuelve las instancias en una lista de ProductDTO
    return [
        Product(
            product_id=product.sku,
            unit_name=product.unit,
            category_name=product.category,
            brand_name=product.brand,
            quantity=product.quantity,
            cost_price=product.cost_price,
            selling_price=product.selling_price,
            reorder_level=product.reorder_level
        ) for product in results
    ]


def _create_GirdView_product_cards(products: list[Product]) -> list[ft.Card]: # Crea las tarjetas de productos
    return [
        ProductCard(product=product, on_click=handle_on_card_button_click)
        for product in products
    ]


product_controller = ProductController() # Controlador de productos

products: list[Product] # Lista de productos en la vista

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handle_on_tap,
    on_change=handle_on_change
)

gird_view = ft.GridView( # Vista de productos
    controls=[
        *_create_GirdView_product_cards(_wrap_productDTO_list(product_controller.get_all()))
    ],
    expand=1,
    runs_count=3,
    max_extent=420,
    child_aspect_ratio=5.5,
    spacing=5,
    run_spacing=5,
)
