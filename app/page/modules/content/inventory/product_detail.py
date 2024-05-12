from re import S
import flet as ft


class Field(ft.Row):
    def __init__(self, property, value):
        super().__init__()
        self.property   = ft.TextButton(text=property, on_click=self.edit_field)
        self.value      = ft.TextField(value=value, read_only=True, border=ft.InputBorder.NONE)
        self.controls   = [
            ft.Row(controls=[self.property], alignment=ft.MainAxisAlignment.START, width=150),
            ft.Row(controls=[self.value], alignment=ft.MainAxisAlignment.START, expand=True),
        ]

    def edit_field(self, event):
        self.value.read_only = False if self.value.read_only else True
        self.value.focus()
        self.update()



class ProductDetail(ft.Card):
    
    def __init__(self, product):
        super().__init__()
        self.product = product
        self.width = 300
        self.expand = True
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
            expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    img,
                    ft.Divider(),
                    Field('SKU', self.product.sku),
                    Field('Unidad', self.product.unit_id),
                    Field('Categoría', self.product.category_id),
                    Field('Marca', self.product.brand_id),
                    Field('Cantidad', self.product.quantity),
                    Field('Precio de compra', self.product.purchase_price),
                    Field('Precio de venta', self.product.sale_price),
                    save_button
                ]
            )
        )
