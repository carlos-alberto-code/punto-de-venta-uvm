import flet as ft


class ProductTable(ft.DataTable):

    def __init__(self, products: list):
        super().__init__()
        self.products = products
        self.sort_functions = {
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
        self.update_table()
    
    @staticmethod
    def create_data_cell(value: str):
        return ft.DataCell(ft.Text(value=value))
    
    def create_data_row(self, product):
        return ft.DataRow(
            cells=[self.create_data_cell(str(getattr(product, attr))) for attr in self.sort_functions.keys()]
        )
    
    def update_table(self):
        self.rows = [self.create_data_row(product) for product in self.products]

    @staticmethod
    def create_data_column(name: str):
        return ft.DataColumn(ft.Text(name))
    
    def sort_by(self, attribute, type):
        reverse_order = not self.sort_order[attribute]
        self.products = sorted(self.products, key=lambda product: type(getattr(product, attribute)), reverse=reverse_order)
        self.sort_order[attribute] = reverse_order
        self.update_table()
    
    def sort_by_key(self, key: str, event: ft.ControlEvent):
        self.sort_functions[key]()
        self.update()
