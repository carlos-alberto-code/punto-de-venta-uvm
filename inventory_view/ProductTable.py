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


column_state_order = {
    column_name.value: True 
    for column_name in ColumnNames
}

column_to_attribute_map = {
    column_name.value: product_attribute.value
    for column_name, product_attribute 
    in zip(ColumnNames, ProductAttributes)
}


class ProductTable(ft.DataTable):

    def __init__(self, products: list):
        super().__init__(
            columns=[
                self._create_data_column(
                    label=column_name.value,
                    on_click=self.sort_products
                ) for column_name in ColumnNames
            ],
            border=ft.border.all(width=1, color=ft.colors.GREY_300),
            border_radius=15,
        )
        self._products = products
        self.update_table()
    
    @property
    def products(self):
        return self._products
    
    @products.setter
    def products(self, products: list):
        self._products = products
        self.update_table()
        self.update()
    
    @staticmethod
    def _create_data_cell(value: str):
        return ft.DataCell(ft.Text(value=value), on_tap=ProductTable.handle_on_tap_cell)

    @staticmethod
    def handle_on_tap_cell(event: ft.ControlEvent):
        cell = event.control
        cell.content = ft.TextField(label='Nuevo valor')
        cell.update()
    
    def _create_data_row(self, product):
        return ft.DataRow(
            cells=[
                self._create_data_cell(value=getattr(product, attr.value))
                for attr in ProductAttributes
            ]
        )
    
    @staticmethod
    def _create_data_column(label: str, on_click):
        return ft.DataColumn(
            label=ft.Text(value=label.capitalize(), color='blue'),
            tooltip=f'Ordenar por {label.lower()}',
            on_sort=on_click,
        )
    
    def update_table(self):
        self.rows = [self._create_data_row(product) for product in self._products]
    
    def sort_products(self, event):
        column_name = event.control.label.value.upper()
        attr_name = column_to_attribute_map[column_name]
        column_state_order[column_name] = not column_state_order[column_name]
        self._products.sort(
            key=lambda product: getattr(product, attr_name),
            reverse=column_state_order[column_name]
        )
        self.update_table()
        self.update()
