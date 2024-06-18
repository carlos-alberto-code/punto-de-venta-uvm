# Aquí se maneja la lógica de los eventos de los diferentes componentes de la vista de la compra
# Además se sigue un principio que es es cada componente se modifica en su contexto.
import flet as ft
from controllers.controllers import ProductController
from purchase_view.ProductViewCard import ProductViewCard
from purchase_view.ItemList import PurchaseList
from business_classes.Product import Product as Product # Data Transfer Object


# HANDLERS ---------------------------------------------------------------------

def handle_on_tap(event: ft.ControlEvent): # Evento tap de la barra de búsqueda
    searcher.close_view()
    products = _wrap_productDTO_list(product_controller.get_all())
    list_view.controls = _create_list_view_product_cards(products)
    list_view.update()
    
def handle_on_change(event: ft.ControlEvent): # Evento de búsqueda en tiempo real
    results = product_controller.search(str(searcher.value))
    products = _wrap_productDTO_list(results)
    list_view.controls = _create_list_view_product_cards(products)
    list_view.update()

def handle_on_add(event: ft.ControlEvent): # Evento de añadir producto a la lista de compras
    product = event.control.data
    purchase_list.add_product(product)
    purchase_list.update()



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


def _create_list_view_product_cards(products: list[Product]) -> list[ft.Card]: # Crea las tarjetas de productos
    return [
        ProductViewCard(product=product, on_add=handle_on_add)
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
        *_create_list_view_product_cards(_wrap_productDTO_list(product_controller.get_all()))
    ],
    spacing=10,
)

purchase_list = PurchaseList(title='Lista de compras')


# SHAPE CONTENT-----------------------------------------------------------------

shape = ft.Row( # Capa general de la vista
    controls=[
        purchase_list,
        ft.Column( # Capa de búsqueda y productos
            [
                searcher,
                list_view
            ],
            expand=True,
        )
    ],
    expand=2,
)
