import flet as ft
from enum import Enum


class ColumnNames(Enum):
    """
    Represents the column names for the inventory table view.
    """
    UNIT = 'UNIDAD'
    CATEGORY = 'CATEGORIA'
    BRAND = 'MARCA'
    QUANTITY = 'CANTIDAD'
    COST_PRICE = 'PRECIO DE COMPRA'
    SELLING_PRICE = 'PRECIO DE VENTA'
    REORDER_LEVEL = 'NIVEL DE REORDEN'

    def __iter__(self):
        yield from self.__dict__.values()


class ProductAttributes(Enum):
    """
    Represents the attributes of a product.
    """
    UNIT = 'unit'
    CATEGORY = 'category'
    BRAND = 'brand'
    QUANTITY = 'quantity'
    COST_PRICE = 'cost_price'
    SELLING_PRICE = 'selling_price'
    REORDER_LEVEL = 'reorder_level'

    def __iter__(self):
        yield from self.__dict__.values()
    
    def __len__(self):
        return len(self.__dict__)


class ProductTable(ft.DataTable):

    def __init__(self, products: list):
        super().__init__()
        self.products = products
        self.sort_functions = {
            'unit': lambda: self._sort_by('unit', lambda x: str(x).lower()),
            'category': lambda: self._sort_by('category', lambda x: str(x).lower()),
            'brand': lambda: self._sort_by('brand', lambda x: str(x).lower()),
            'quantity': lambda: self._sort_by('quantity', int),
            'cost_price': lambda: self._sort_by('cost_price', float),
            'selling_price': lambda: self._sort_by('selling_price', float),
            'reorder_level': lambda: self._sort_by('reorder_level', int),
        }
        self.sort_order = {key: True for key in self.sort_functions.keys()}
        self.columns=[
            ft.DataColumn(ft.TextButton('UNIDAD', on_click=lambda event: self._sort_by_key('unit', event))),
            ft.DataColumn(ft.TextButton('CATEGORÍA', on_click=lambda event: self._sort_by_key('category', event))),
            ft.DataColumn(ft.TextButton('MARCA', on_click=lambda event: self._sort_by_key('brand', event))),
            ft.DataColumn(ft.TextButton('CANTIDAD', on_click=lambda event: self._sort_by_key('quantity', event))),
            ft.DataColumn(ft.TextButton('PRECIO DE COMPRA', on_click=lambda event: self._sort_by_key('cost_price', event))),
            ft.DataColumn(ft.TextButton('PRECIO DE VENTA', on_click=lambda event: self._sort_by_key('selling_price', event))),
            ft.DataColumn(ft.TextButton('STOCK MÍNIMO', on_click=lambda event: self._sort_by_key('reorder_level', event))),
        ]
        self.update_table()
    
    @staticmethod
    def _create_data_cell(value: str):
        return ft.DataCell(ft.Text(value=value))
    
    def _create_data_row(self, product):
        return ft.DataRow(
            cells=[self._create_data_cell(str(getattr(product, attr))) for attr in self.sort_functions.keys()]
        )
    
    def update_table(self):
        self.rows = [self._create_data_row(product) for product in self.products]

    def create_data_column(self, label: str, on_click):
        return ft.DataColumn(ft.TextButton(label, on_click=on_click))
    
    def _sort_by(self, attribute, type):
        reverse_order = not self.sort_order[attribute]
        self.products = sorted(self.products, key=lambda product: type(getattr(product, attribute)), reverse=reverse_order)
        self.sort_order[attribute] = reverse_order
        self.update_table()
    
    def _sort_by_key(self, key: str, event: ft.ControlEvent):
        self.sort_functions[key]()
        self.update()
