import flet as ft


class ProductTable(ft.DataTable):

    def __init__(self, products: list):
        super().__init__()
        self.products = products
        self.sort_functions = {
            # 'sku': lambda: self.sort_by('sku', int),
            'unit': lambda: self.sort_by('unit', lambda x: str(x).lower()),
            'category': lambda: self.sort_by('category', lambda x: str(x).lower()),
            'brand': lambda: self.sort_by('brand', lambda x: str(x).lower()),
            'quantity': lambda: self.sort_by('quantity', int),
            'cost_price': lambda: self.sort_by('cost_price', float),
            'selling_price': lambda: self.sort_by('selling_price', float),
            'reorder_level': lambda: self.sort_by('reorder_level', int),
        }
        self.sort_order = {key: True for key in self.sort_functions.keys()}
        self.columns=[

            ft.DataColumn(ft.TextButton('UNIDAD', on_click=lambda event: self.sort_by_key('unit', event))),
            ft.DataColumn(ft.TextButton('CATEGORÍA', on_click=lambda event: self.sort_by_key('category', event))),
            ft.DataColumn(ft.TextButton('MARCA', on_click=lambda event: self.sort_by_key('brand', event))),
            ft.DataColumn(ft.TextButton('CANTIDAD', on_click=lambda event: self.sort_by_key('quantity', event))),
            ft.DataColumn(ft.TextButton('PRECIO DE COMPRA', on_click=lambda event: self.sort_by_key('cost_price', event))),
            ft.DataColumn(ft.TextButton('PRECIO DE VENTA', on_click=lambda event: self.sort_by_key('selling_price', event))),
            ft.DataColumn(ft.TextButton('STOCK MÍNIMO', on_click=lambda event: self.sort_by_key('reorder_level', event))),
        ]
        self.rows=[
            ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(product.unit))),
                ft.DataCell(ft.Text(str(product.category))),
                ft.DataCell(ft.Text(str(product.brand))),
                ft.DataCell(ft.Text(str(product.quantity))),
                ft.DataCell(ft.Text(str(product.cost_price))),
                ft.DataCell(ft.Text(str(product.selling_price))),
                ft.DataCell(ft.Text(str(product.reorder_level))),
            ],
            ) for product in self.products
            
        ]
    
    def sort_by(self, attribute, type):
        reverse_order = not self.sort_order[attribute]
        self.products = sorted(self.products, key=lambda product: type(getattr(product, attribute)), reverse=reverse_order)
        self.sort_order[attribute] = reverse_order
        self.update_table()
    
    def update_table(self):
        self.rows = [ # type: ignore
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(product.unit))),
                    ft.DataCell(ft.Text(str(product.category))),
                    ft.DataCell(ft.Text(str(product.brand))),
                    ft.DataCell(ft.Text(str(product.quantity))),
                    ft.DataCell(ft.Text(str(product.cost_price))),
                    ft.DataCell(ft.Text(str(product.selling_price))),
                    ft.DataCell(ft.Text(str(product.reorder_level))),
                ],
            ) for product in self.products
        ]
    
    def sort_by_key(self, key: str, event: ft.ControlEvent):
        self.sort_functions[key]()
        self.update()