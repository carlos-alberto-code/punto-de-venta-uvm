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
            'SKU': lambda: self.sort_by('sku', int),
            'UNIDAD': lambda: self.sort_by('unit', lambda x: str(x).lower()),
            'CATEGORÍA': lambda: self.sort_by('category', str),
            'MARCA': lambda: self.sort_by('brand', str),
            'CANTIDAD': lambda: self.sort_by('quantity', int),
            'PRECIO DE COMPRA': lambda: self.sort_by('purchase_price', float),
            'PRECIO DE VENTA': lambda: self.sort_by('sale_price', float),
            'STOCK MÍNIMO': lambda: self.sort_by('minimum_stock', int),
        }
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
        self.products = sorted(self.products, key=lambda product: type(getattr(product, attribute)))
        self.update_table()

    def update_table(self):
        self.controls[1].rows = [
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
        self.sort_functions['SKU']()
        event.page.update()

    def sort_by_unit(self, event: ft.ControlEvent):
        self.sort_functions['UNIDAD']()
        event.page.update()

    def sort_by_category(self, event: ft.ControlEvent):
        self.sort_functions['CATEGORÍA']()
        event.page.update()
    
    def sort_by_brand(self, event: ft.ControlEvent):
        self.sort_functions['MARCA']()
        event.page.update()
    
    def sort_by_quantity(self, event: ft.ControlEvent):
        self.sort_functions['CANTIDAD']()
        event.page.update()
    
    def sort_by_purchase_price(self, event: ft.ControlEvent):
        self.sort_functions['PRECIO DE COMPRA']()
        event.page.update()

    def sort_by_sale_price(self, event: ft.ControlEvent):
        self.sort_functions['PRECIO DE VENTA']()
        event.page.update()
    
    def sort_by_minimum_stock(self, event: ft.ControlEvent):
        self.sort_functions['STOCK MÍNIMO']()
        event.page.update()
    