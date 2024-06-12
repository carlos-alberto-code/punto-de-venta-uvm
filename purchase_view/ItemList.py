import flet as ft
from datetime import datetime as dt
# from controllers.controllers import 
from purchase_view.ProductDTO import ProductDTO as Product
from purchase_view.ProviderSearcher import Searcher


class ProductSet(set[Product]):
    def __init__(self):
        super().__init__()
    
    def add_product(self, product: Product):
        self.add(product)
    
    def remove_product(self, product: Product):
        self.remove(product)
    
    def clear_products(self):
        self.clear()



class ItemSet(ft.Card):

    products: ProductSet = ProductSet()

    def __init__(self):
        super().__init__(
            width=350,
            height=600,
            elevation=10,
        )
    
    def add_item(self, product: Product):
        ItemSet.products.add_product(product=product)
        self._update_items()
    
    def remove_item(self, product: Product):
        ItemSet.products.remove_product(product=product)
        self._update_items()
    
    def clear_items(self):
        ItemSet.products.clear_products()
        self._update_items()
    

    # Evento de click en el botón de eliminar
    def handle_on_delete(self, event: ft.ControlEvent):
        self.remove_item(event.control.data)

    # Estas funciones son para la capa de vista formulario
    
    def _update_items(self):
        self.content = ft.Column(
            [
                self._create_item(product)
                for product in ItemSet.products
            ]
        )
        self.update()

    def _create_item(self, product: Product):
        return ft.Card(
            width=350,
            height=70,
            content=ft.ListTile(
                leading=ft.Image(
                    src='https://images.pexels.com/photos/1002649/pexels-photo-1002649.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                    fit=ft.ImageFit.COVER,
                    width=50,
                    height=50,
                    border_radius=10,
                ),
                title=ft.Text(value=product.name, size=15),
                subtitle=ft.Text(value=f'Precio: ${product.cost_price}', size=12),
                trailing=ft.IconButton(
                    data=product,
                    icon=ft.icons.DELETE,
                    on_click=self.handle_on_delete,
                )
            )
        )


class WidgetItemSet(ft.ListView): # Capa para anidar productos (items)
    
        def __init__(self):
            super().__init__(
                controls=[
                    ft.Text(f'Producto {i}')
                    for i in range(10)
                ],
                # spacing=10,
                # divider_thickness=4,
                # padding=15,
            )



class WidgetPurchaseList(ft.Card): # Capa general para representar la lista de compras

    def __init__(self):
        super().__init__(
            elevation=10,
            expand=True,
            width=350,
        )
        date = dt.now()
        self.content=ft.ListView(
            controls=[
                # Texto para representar el título: Lista de compras
                ft.Row([ft.Text('Lista de compras', size=25)], alignment=ft.MainAxisAlignment.CENTER),
                # Texto para representar el día de hoy
                ft.Row([ft.Text(f'{date.date()}', size=15)], alignment=ft.MainAxisAlignment.CENTER),
                # Barra de búsqueda para buscar proveedores
                Searcher(),
            ],
            spacing=15,
            padding=15,
        )
