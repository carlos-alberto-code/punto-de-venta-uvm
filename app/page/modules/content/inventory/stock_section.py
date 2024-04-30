import flet as ft

from controllers.products_controller import ProductController


_search_bar = ft.TextField(
    label='Buscar',
)

_filter_by = ft.Dropdown(
    label='Filtrar por',
    options=[
        ft.dropdown.Option(text='Categoría'),
        ft.dropdown.Option(text='Unidad'),
        ft.dropdown.Option(text='Marca'),
    ]
)


class StockSection(ft.Column):
    
    def __init__(self):
        super().__init__()
        self.products = ProductController.get_all()
        self.spacing = 20
        self.sort_functions = {
            'sku': lambda: self.sort_by('sku', int),
            'unit': lambda: self.sort_by('unit', lambda x: str(x).lower()),
            'category': lambda: self.sort_by('category', lambda x: str(x).lower()),
            'brand': lambda: self.sort_by('brand', lambda x: str(x).lower()),
            'quantity': lambda: self.sort_by('quantity', int),
            'purchase_price': lambda: self.sort_by('purchase_price', float),
            'sale_price': lambda: self.sort_by('sale_price', float),
            'minimum_stock': lambda: self.sort_by('minimum_stock', int),
        }
        self.sort_order = {key: True for key in self.sort_functions.keys()}
        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    _search_bar,
                    _filter_by
                ],
            ), # Row End
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.TextButton('SKU', on_click=self.sort_by_sku)),
                    ft.DataColumn(ft.TextButton('UNIDAD', on_click=self.sort_by_unit)),
                    ft.DataColumn(ft.TextButton('CATEGORÍA', on_click=self.sort_by_category)),
                    ft.DataColumn(ft.TextButton('MARCA', on_click=self.sort_by_brand)),
                    ft.DataColumn(ft.TextButton('CANTIDAD', on_click=self.sort_by_quantity)),
                    ft.DataColumn(ft.TextButton('PRECIO DE COMPRA', on_click=self.sort_by_purchase_price)),
                    ft.DataColumn(ft.TextButton('PRECIO DE VENTA', on_click=self.sort_by_sale_price)),
                    ft.DataColumn(ft.TextButton('STOCK MÍNIMO', on_click=self.sort_by_minimum_stock)),
                    ft.DataColumn(ft.TextButton('DESCRIPCIÓN')),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(product.sku))),
                            ft.DataCell(ft.Text(str(product.unit))),
                            ft.DataCell(ft.Text(str(product.category))),
                            ft.DataCell(ft.Text(str(product.brand))),
                            ft.DataCell(ft.Text(str(product.quantity))),
                            ft.DataCell(ft.Text(str(product.purchase_price))),
                            ft.DataCell(ft.Text(str(product.sale_price))),
                            ft.DataCell(ft.Text(str(product.minimum_stock))),
                            ft.DataCell(ft.Text(product.description)),
                        ]
                    ) for product in self.products
                    
                ]
            )
        ]

    def sort_by(self, attribute, type):
        reverse_order = not self.sort_order[attribute]
        self.products = sorted(self.products, key=lambda product: type(getattr(product, attribute)), reverse=reverse_order)
        self.sort_order[attribute] = reverse_order
        self.update_table()

    def update_table(self):
        self.controls[1].rows = [ # type: ignore
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(product.sku))),
                    ft.DataCell(ft.Text(str(product.unit))),
                    ft.DataCell(ft.Text(str(product.category))),
                    ft.DataCell(ft.Text(str(product.brand))),
                    ft.DataCell(ft.Text(str(product.quantity))),
                    ft.DataCell(ft.Text(str(product.purchase_price))),
                    ft.DataCell(ft.Text(str(product.sale_price))),
                    ft.DataCell(ft.Text(str(product.minimum_stock))),
                    ft.DataCell(ft.Text(product.description)),
                ]
            ) for product in self.products
        ]

    def sort_by_sku(self, event: ft.ControlEvent):
        self.sort_functions['sku']()
        event.page.update()

    def sort_by_unit(self, event: ft.ControlEvent):
        self.sort_functions['unit']()
        event.page.update()

    def sort_by_category(self, event: ft.ControlEvent):
        self.sort_functions['category']()
        event.page.update()
    
    def sort_by_brand(self, event: ft.ControlEvent):
        self.sort_functions['brand']()
        event.page.update()
    
    def sort_by_quantity(self, event: ft.ControlEvent):
        self.sort_functions['quantity']()
        event.page.update()
    
    def sort_by_purchase_price(self, event: ft.ControlEvent):
        self.sort_functions['purchase_price']()
        event.page.update()

    def sort_by_sale_price(self, event: ft.ControlEvent):
        self.sort_functions['sale_price']()
        event.page.update()
    
    def sort_by_minimum_stock(self, event: ft.ControlEvent):
        self.sort_functions['minimum_stock']()
        event.page.update()
    