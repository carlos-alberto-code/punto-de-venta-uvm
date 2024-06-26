# En el contexto del punto de venta (tienda) se manejan los siguientes eventos:
# - handle_on_tap: Evento tap de la barra de búsqueda (si existe)
# - handle_on_change: Evento de búsqueda en tiempo real
# - handle_on_add_button_click: Evento de click en el botón de la tarjeta
# - handle_on_card_button_click: Evento de click en el botón de la tarjeta
# - handle_on_remove_button_click: Evento de click en el botón de la tarjeta (de la lista de compra)
# - handle_on_clear_button_click: Evento de click en el botón de limpiar la lista de compra
# - handle_on_process_button_click: Evento de click en el botón de procesar la compra

import flet as ft

from modules.store_view.ProductCard import ProductCard
from modules.store_view.ProductItem import ProductItem
from modules.store_view.ProductDTO import ProductDTO as Product # Data Transfer Object


from components.ProductListView import ProductListView
from controllers.dto_controllers.product_dto_controller import ProductDTOController


# HANDLERS ---------------------------------------------------------------------

def handle_on_searcher_tap(event: ft.ControlEvent):
    searcher.close_view()
    products = product_controller.get_all()
    product_list_view.products = products
    product_list_view.update()
    
def handle_on_searcher_change(event: ft.ControlEvent):
    results = product_controller.search(str(searcher.value))
    product_list_view.products = results
    product_list_view.update()

def handle_on_add_button_click(event: ft.ControlEvent):
    button: ft.IconButton = event.control
    form_items.add(button.data)
    product_form.content = ft.Column(
        [create_form_item_cart(product) for product in form_items]
    )
    product_form.update()

def create_form_item(product: Product): # Crea un item del formulario de compra
    return ProductCard(product=product)

def create_form_item_cart(product: Product): # Crea un item del formulario de compra
    return ProductItem(product=product,on_click=remove_form_item_cart)

def remove_form_item_cart(event: ft.ControlEvent):
    button = event.control
    product = button.data
    form_items.remove(product)
    product_form.content = ft.Column(
        [create_form_item_cart(product) for product in form_items]
    )
    product_form.update()


# CONTEXT ----------------------------------------------------------------------

product_controller = ProductDTOController()

products: list[Product] # Lista de productos en la vista

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handle_on_searcher_tap,
    on_change=handle_on_searcher_change
)

product_list_view = ProductListView(
    on_add_button_click=handle_on_add_button_click,
)
product_list_view.products = product_controller.get_all()

form_items = set()
product_form = ft.Card(
    width=350,
    height=800,
    elevation=10,
)

# SHAPE CONTENT-----------------------------------------------------------------

StoreShape = ft.ResponsiveRow( # Capa general de la vista
    [
        ft.Column( # Capa de búsqueda y productos
            [
                ft.Container( # Capa de búsqueda
                    #width=900,
                    height=50,
                    content=searcher,
                ),
                ft.Container( # Capa de productos
                    # Abarca el resto de la pantalla
                    #width=900,
                    height=800,
                    content=product_list_view,
                ),
            ],
            col=8,
        ),
        ft.Container( # Capa de formulario
            #width=350,
            height=900,
            content=product_form,
            col=4,
        ),
    ]
)
