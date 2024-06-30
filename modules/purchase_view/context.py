# Aquí se maneja la lógica de los eventos de los diferentes componentes de la vista de la compra
# Además se sigue un principio que es es cada componente se modifica en su contexto.
import flet as ft

from business_objects.Product                           import Product
from components.ProductList                             import ProductList
from components.ShoppingCart                            import ShoppingCart
from repository.dto_controllers.product_dto_controller  import ProductDTOController
from components.product_cards                           import ProductCard, ProductCardFactory, CardType

# HANDLERS ---------------------------------------------------------------------
def handler_on_remove_button_card_click(event: ft.ControlEvent): # Al presionar en el botón de remover
    button = event.control
    card: ProductCard = button.data['card']
    shopping_cart.remove_product_card(card)
    shopping_cart.update()
    # Ready

def handler_on_add_button_card_click(event: ft.ControlEvent): # Al presionar en el botón de añadir
    button = event.control
    product: Product = button.data['product']
    existing_card = next((card for card in shopping_cart.product_list_view.product_cards if card.data['product'].product_id == product.product_id), None)
    if not existing_card:
        card: ProductCard = cards_factory.create_product_card(
            product=product,
            card_type=CardType.PURCHASE,
            on_button_card_click=handler_on_remove_button_card_click
        )
        shopping_cart.add_product_card(card)
        calculate_total(event)
        shopping_cart.update()
    # Ready

def handler_on_clear_button_click(event: ft.ControlEvent): # Al presionar en el botón de limpiar
    shopping_cart.clear_all_cards()
    shopping_cart.update()
    calculate_total(event)
    # Ready

def handler_on_process_button_click(event: ft.ControlEvent): # Al presionar en el botón de procesar
    pass

def handler_on_searcher_tap(event: ft.ControlEvent): # Al presionar en la barra de búsqueda
    searcher.close_view('')
    product_list_view.product_cards = [
        cards_factory.create_product_card(
            product=product,
            card_type=CardType.DISPLAY,
            on_button_card_click=handler_on_add_button_card_click
        ) for product in product_controller.get_all()
    ]
    product_list_view.update()
    # Ready

def handle_on_searcher_change(event: ft.ControlEvent): # Al cambiar el texto en la barra de búsqueda
    search_term = searcher.value
    results = product_controller.search(str(search_term))
    if results:
        product_list_view.product_cards = [
            cards_factory.create_product_card(
                product=product,
                card_type=CardType.DISPLAY,
                on_button_card_click=handler_on_add_button_card_click
            ) for product in results
        ]
        product_list_view.update()
    # Ready

def calculate_total(event: ft.ControlEvent):
    total = 0
    for card in shopping_cart.product_list_view.product_cards:
        total += float(card.get_total_card) if card.get_total_card else 0
    shopping_cart.total_text_value = total
    shopping_cart.update()
    # Ready

# CONTEXT ----------------------------------------------------------------------
cards_factory = ProductCardFactory()
product_controller = ProductDTOController() # Controlador de productos

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handler_on_searcher_tap,
    on_change=handle_on_searcher_change
)

product_list_view = ProductList() # Lista de productos en la vista
product_list_view.product_cards = [
    cards_factory.create_product_card(
        product=product,
        card_type=CardType.DISPLAY,
        on_button_card_click=handler_on_add_button_card_click
    ) for product in product_controller.get_all()
]
shopping_cart = ShoppingCart(
    on_clear_button_click=handler_on_clear_button_click,
    on_calculate_button_click=calculate_total,
)

# SHAPE CONTENT-----------------------------------------------------------------

shape = ft.ResponsiveRow( # Capa general de la vista
    controls=[
        ft.Container(
            content=shopping_cart,
            expand=True,
            col=4.5
        ),
        ft.Column( # Capa de búsqueda y productos
            [   
                ft.Container(
                    height=50,
                    content=searcher,
                ),
                ft.Container(
                    content=product_list_view,
                    expand=True
                ),
            ],
            col=7.5,
        )
    ],
    spacing=0
)
