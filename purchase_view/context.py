# Aquí se maneja la lógica de los eventos de los diferentes componentes de la vista de la compra
# Además se sigue un principio que es es cada componente se modifica en su contexto.
import flet as ft
from controllers.controllers import ProductController
from purchase_view.ProductCard import ProductCard
from business_classes.Product import Product as Product # Data Transfer Object


# HANDLERS ---------------------------------------------------------------------

def handle_on_tap(event: ft.ControlEvent): # Evento tap de la barra de búsqueda
    searcher.close_view()
    products = _wrap_productDTO_list(product_controller.get_all())
    list_view.controls = _create_GirdView_product_cards(products)
    list_view.update()
    
def handle_on_change(event: ft.ControlEvent): # Evento de búsqueda en tiempo real
    results = product_controller.search(str(searcher.value))
    products = _wrap_productDTO_list(results)
    list_view.controls = _create_GirdView_product_cards(products)
    list_view.update()

def handle_on_card_button_click(event: ft.ControlEvent): # Evento de click en el botón de la tarjeta
    button = event.control
    form_items.append(button.data)
    product_form.content = ft.Column(
        [create_form_item(product) for product in form_items]
    )
    product_form.update()

def create_form_item(product: Product): # Crea un item del formulario de compra
    return ProductCard(product=product)


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


# CONTEXT ----------------------------------------------------------------------

product_controller = ProductController() # Controlador de productos

products: list[Product] # Lista de productos en la vista

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handle_on_tap,
    on_change=handle_on_change
)

list_view = ft.ListView( # Vista de productos
    controls=[
        *_create_GirdView_product_cards(_wrap_productDTO_list(product_controller.get_all()))
    ],
    spacing=10,
)

form_items = []
product_form = ft.Card(
    width=400,
    elevation=10,
)


# SHAPE CONTENT-----------------------------------------------------------------

shape = ft.Row( # Capa general de la vista
    controls=[
        product_form,
        ft.Column( # Capa de búsqueda y productos
            [
                searcher,
                list_view,
            ],
            expand=True
        )
    ]
)
