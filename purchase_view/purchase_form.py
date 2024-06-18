import flet as ft
from business_classes.Product import Product # Data Transfer Object
from components.counters import Counter



class ProductFormCard(ft.Card):
    def __init__(self, product: Product, on_delete=None):
        super().__init__(
            width=250,
        )
        self.product = product
        self.on_delete = on_delete
        
        self.data: Product = product

        self.counter = Counter(on_click=self.handle_on_counter_change)
        self.cost_textfield = self.create_textfield(product.cost_price)
        self.cost_textfield.on_change = self.handle_on_cost_change
        self.selling_textfield = self.create_textfield(product.selling_price)
        self.total_text = self.create_text(product.total_cost)

        self.content = self.create_content()

    def create_content(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.create_icon(),
                    self.create_text(self.product.name),
                    self.create_row('Cantidad:', self.counter),
                    self.create_row('Compra:', self.cost_textfield),
                    self.create_row('Venta:', self.selling_textfield),
                    self.create_row(label='Total compra:', control=self.total_text),
                    self.create_icon_button()
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
            padding=10,
        )

    def create_icon(self):
        return ft.Icon(ft.icons.SHOPPING_BAG, size=30)

    def create_text(self, value):
        return ft.Text(value=str(value), size=12)

    def create_row(self, label, control):
        return ft.Row(
            controls=[
                ft.Text(label, size=12),
                control
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def create_textfield(self, value):
        return ft.TextField(value=str(value), text_size=12, text_vertical_align=ft.VerticalAlignment.START, border=ft.InputBorder.NONE, text_align=ft.TextAlign.END, expand=True)

    def create_icon_button(self):
        return ft.IconButton(icon=ft.icons.DELETE)
    
    def handle_on_counter_change(self, event:ft.ControlEvent):
        self.product.quantity = int(self.counter.value)
        self.total_text.value = str(self.product.total_cost)
        self.total_text.update()
        self.data = self.product
    
    def handle_on_cost_change(self, event: ft.ControlEvent):
        self.product.cost_price = float(self.cost_textfield.value or 0)
        self.total_text.value = str(self.product.total_cost)
        self.total_text.update()
        # Cambiar el precio de venta si el costo cambia (20% de ganancia)
        self.product.selling_price = round(self.product.cost_price * 1.2, 2)
        self.selling_textfield.value = str(self.product.selling_price)
        self.selling_textfield.update()
        self.data = self.product


class PurchaseForm(ft.Card):

    def __init__(self):
        super().__init__(
            width=400,
            elevation=10,
        )
        self.products: set[Product] = set()
        self.content
    
    def add_item(self, product: Product):
        pass
    
    def create_card(self, product: Product):
        return ProductFormCard(product=product)
