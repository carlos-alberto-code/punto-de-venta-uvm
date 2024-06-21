import flet as ft
from store_view.ProductDTO import ProductDTO as Product
from components.counters import IntCounter

class ItemList(ft.Card):

    products: list[Product] = []

    def __init__(self):
        super().__init__(
            width=350,
            height=600,
            elevation=10,
        )
    
    def add_item(self, item: Product):
        self._add_product(product=item)
        self._update_items()
    
    def delete_item(self, item: Product):
        self._remove_product(item=item)
        self._update_items()
    
    def clear_items(self):
        self._clear_products()
        self._update_items()
    

    # Evento de click en el botón de eliminar
    def handle_on_delete(self, event: ft.ControlEvent):
        self.delete_item(event.control.data)

    # Estas funciones son para la capa de vista formulario
    
    def _update_items(self):
        self.content = ft.Column(
            [
                self._create_item(product)
                for product in ItemList.products
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
                ),
            )
        )
    
    # Las siguientes funciones sólo operan para la lista de productos y no para la capa de vista formulario

    def _remove_product(self, item: Product):
        if item in ItemList.products:
            ItemList.products.remove(item)
    
    def _clear_products(self):
        ItemList.products.clear()

    def _add_product(self, product: Product):
        ItemList.products.append(product)
