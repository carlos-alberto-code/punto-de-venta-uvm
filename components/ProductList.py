import flet as ft

from business_classes.Product   import Product
from components.ProductCard     import ProductCard


class ProductList(ft.ListView):
    '''
    El propósito de esta clase es que pueda anidar ProductCard's. La ingesta de ProductCard's puede darse de muchas formas, y es por eso que sea ha diseñado de esta forma; puede provenir de una fábrica de ProductCard's, puede implementarse mediante herencia y recibir un "tipo" de ProductCard, o simplemente puede ser una lista de ProductCard's que se añaden a la lista de ProductListView de forma configurable.

    Esta clase tiene métodos para añadir, remover y limpiar ProductCard's de la lista, así como también para obtener el número de ProductCard's que contiene (para el caso en donde es necesario saber el número de items que hay en la lista).

    Esta clase debría poder usarse para mostrar una lista de productos con un aspecto ligeramente grande, por ejemplo, en lugares donde se necesita buscar productos y poder seleccionarlos para añadirlos a una lista de compra. Pero también debería ser posible usarla para mostrar esos productos con otra presentación dentro de la lista de compra. Para ello se ha establecidgo el ProductCard como interfaz (aunque no es una interfaz).

    Se permitieron los getters y setters a nivel general para los controles para los casos en donde se deben inyectar muchos ProductCard's, por ejemplo, la muestra general de productos.
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
