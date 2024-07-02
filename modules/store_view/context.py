# TODO: Implementar funciones en la base de datos para que al procesar la compra, se actualice el inventario
# TODO: Guardar la compra en la base de datos
# TODO: Permitir que los productos puedan ser ordenados en función de ciertas propiedades
# TODO: Permitir que los productos puedan ser filtrados en función de ciertas propiedades

import flet as ft
from typing import Any
from datetime import datetime

from business_objects.Sale import Sale
from business_objects.SaleDetail import SaleDetail
from repository.sales_register_management import SalesRegisterManagement

from modules.store_view.ticket                          import Ticket
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

def handler_on_add_button_card_click(event: ft.ControlEvent): # Al presionar en el botón de añadir
    button = event.control
    product: Product = button.data['product']
    if product.quantity > 0:
        existing_card = next(
            (
                card for card in shopping_cart.product_list_view.product_cards
                if card.data['product'].product_id == product.product_id # type: ignore
            ), None
        )
        if not existing_card:
            card: ProductCard = cards_factory.create_product_card(
                product=product,
                card_type=CardType.SELLING,
                on_button_card_click=handler_on_remove_button_card_click
            )
            shopping_cart.add_product_card(card)
            calculate_total(event)
            shopping_cart.update()

def handler_on_clear_button_click(event: ft.ControlEvent): # Al presionar en el botón de limpiar
    shopping_cart.clear_all_cards()
    shopping_cart.update()
    calculate_total(event)

def handler_on_process_button_click(event: ft.ControlEvent): # Al presionar en el botón de procesar
    if len(shopping_cart.product_list_view.product_cards) > 0:
        products: list[tuple] = []
        total = 0
        sale_details: list[SaleDetail] = []
        for card in shopping_cart.product_list_view.product_cards:
            total += card.product.selling_price * card.quantity
            products.append(
                (
                    card.quantity,
                    card.product.name,
                    card.product.selling_price,
                    card.product.selling_price * card.quantity
                )
            )
            sale_details.append(
                SaleDetail(
                    product=card.product,
                    quantity=card.quantity,
                )
            )
        date = shopping_cart.date
        hour = shopping_cart.time
        
        sale = Sale(
            id=None,
            customer=None,
            datetime=datetime.now(),
            total=total,
            sale_details=sale_details
        )

        sales_register_management = SalesRegisterManagement()
        sales_register_management.register_sale(sale=sale)
        ticket = Ticket(
            business_name='Tienda de abarrotes',
            date=str(date),
            hour=str(hour),
            products=products,
            total=total,
        )
        ticket.build_ticket()
        ticket.show_in_browser()
        shopping_cart.clear_all_cards()
        shopping_cart.update()
        product_list_view.product_cards = [
            cards_factory.create_product_card(
                product=product,
                card_type=CardType.DISPLAY,
                on_button_card_click=handler_on_add_button_card_click
            ) for product in product_controller.get_all()
        ]
        product_list_view.update()
    
    

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
                on_button_card_click=handler_on_add_button_card_click,
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
product_controller = ProductDTOController()

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handler_on_searcher_tap,
    on_change=handle_on_searcher_change
)
product_list_view = ProductList()
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
    on_process_button_click=handler_on_process_button_click
)

# SHAPE CONTENT-----------------------------------------------------------------

StoreShape = ft.ResponsiveRow( # Capa general de la vista
    [
        ft.Column( # Capa de búsqueda y productos
            [
                ft.Container( # Capa de búsqueda
                    height=50,
                    content=searcher,
                ),
                ft.Container( # Capa de productos
                    content=product_list_view,
                    expand=True,
                ),
            ],
            col=7.5,
        ),
        ft.Container( # Capa de formulario
            content=shopping_cart,
            expand=True,
            col=4.5,
        ),
    ],
    spacing=0,
)
