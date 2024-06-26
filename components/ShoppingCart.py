import flet as ft
from business_classes.Product import Product
from components.ProductList import ProductList

class ShoppingCart(ft.Card):

    def __init__(self):
        super().__init__()
        self.product_list_view = ProductList()
        self.content = ft.Column(
            [
                ft.Text('Carrito de compras', size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
            ]
        )
    
    def add_product(self, product: Product):
        pass

'''
Este es el contexto en donde se determina el tipo de ProductCard que se visualizará en el ProductListView. Se puede usar una fábrica para construir un determinado tipo de ProductCard o se puede usar la clase ProductCard e inyectarle los controles de presentación que se requieren. 
'''