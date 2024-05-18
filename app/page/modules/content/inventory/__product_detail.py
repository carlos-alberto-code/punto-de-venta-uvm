from re import S
import flet as ft


class Field(ft.Row):
    def __init__(self, property, value):
        super().__init__()
        self.property   = ft.TextButton(text=property, on_click=self.edit_field)
        self.value      = ft.TextField(value=value, read_only=True, border=ft.InputBorder.NONE, expand=True)
        self.controls   = [
            ft.Row(controls=[self.property], alignment=ft.MainAxisAlignment.START, width=150),
            ft.Row(controls=[self.value], alignment=ft.MainAxisAlignment.START, expand=True),
        ]

    def edit_field(self, event):
        self.value.read_only = False if self.value.read_only else True
        self.value.focus()
        self.update()



class ProductDetail(ft.Card):
    # TODO: A la hora de cambiar una propiedad, debería mostrar una lista de opciones para seleccionar, cómo en el SearchBarFilter, y permitir el registro de una nueva.
    
    
    def __init__(self, product):
        super().__init__()
        self.product = product
        self.elevation = 5
        self.width = 300
        self.height = 650
        img = ft.Image(
            src='https://images.pexels.com/photos/335257/pexels-photo-335257.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            width=150,
            height=150,
            fit=ft.ImageFit.COVER,
            border_radius=30,
        )
        save_button = ft.ElevatedButton(
            text='Guardar',
            icon='save',
            # on_click=self.save_product
        )
        self.content = ft.Container(
            padding=10,
            # expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    img,
                    ft.Divider(),
                    # Field('SKU', self.product.sku),
                    Field('Unidad', self.product.unit),
                    Field('Categoría', self.product.category),
                    Field('Marca', self.product.brand),
                    Field('Cantidad', self.product.quantity),
                    Field('Precio de compra', self.product.cost_price),
                    Field('Precio de venta', self.product.selling_price),
                    save_button
                ]
            )
        )
