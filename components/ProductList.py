import flet as ft

from business_classes.Product   import Product
from components.ProductCard     import ProductCard


class ProductList(ft.ListView):
    '''
    Clase que representa una lista de productos.

    Esta clase permite añadir, remover y limpiar ProductCard's de la lista, así como obtener el número de ProductCard's que contiene.

    Métodos disponibles:
    - add_product_card(product_card: ProductCard): Añade un ProductCard a la lista.
    - remove_product_card(product_card: ProductCard): Remueve un ProductCard de la lista.
    - clear_product_cards(): Limpia la lista de ProductCard's.
    
    Interfaces públicas:
    - number_of_product_cards: Propiedad de solo lectura que devuelve el número de ProductCard's en la lista.
    - product_cards: Propiedad de solo lectura que devuelve la lista de ProductCard's en la lista.
    - product_cards(product_cards: list[ProductCard]): Propiedad que permite establecer la lista de ProductCard's en la lista.

    Ejemplo de uso adecuado:
    ```python
    # Crear una instancia de ProductList
    product_list = ProductList()

    # Crear una instancia de ProductCard
    product_card = ProductCard()

    # Añadir el ProductCard a la lista
    product_list.add_product_card(product_card)

    # Obtener el número de ProductCard's en la lista
    num_cards = product_list.number_of_product_cards

    # Obtener la lista de ProductCard's en la lista
    cards = product_list.product_cards

    # Establecer una nueva lista de ProductCard's en la lista
    new_cards = [ProductCard(), ProductCard()]
    product_list.product_cards = new_cards

    # Remover un ProductCard de la lista
    product_list.remove_product_card(product_card)

    # Limpiar la lista de ProductCard's
    product_list.clear_product_cards()
    ```
    '''
    def __init__(self, product_cards: list[ProductCard] = []):
        super().__init__()
        self.controls: list[ProductCard] = product_cards
    
    @property
    def number_of_product_cards(self) -> int:
        return len(self.controls)
        
    @property
    def product_cards(self) -> list[ProductCard]:
        return self.controls
    
    @product_cards.setter
    def product_cards(self, product_cards: list[ProductCard]) -> None:
        self.controls = product_cards
    
    def add_product_card(self, product_card: ProductCard):
        self.controls.append(product_card)
    
    def remove_product_card(self, product_card: ProductCard):
        self.controls.remove(product_card)
    
    def clear_product_cards(self):
        self.controls.clear()
