import flet as ft
from enum import Enum
from typing import Callable, Optional, List

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


# class ProductAttributesTypes(Enum):
#     """
#     Represents the attribute types for a product.
#     """
#     UNIT = str
#     CATEGORY = str
#     BRAND = str
#     QUANTITY = int
#     COST_PRICE = float
#     SELLING_PRICE = float
#     REORDER_LEVEL = int

#     def __iter__(self):
#         yield from self.__dict__.values()


def create_column(label: str, on_sort: Optional[Callable] = None,) -> ft.DataColumn:
    """
    Create a data column for a table view.

    Args:
        label (str): The label of the column.
        on_sort (Optional[Callable], optional): The function to be called when the column is sorted. Defaults to None.
        is_numeric (bool, optional): Indicates whether the column contains numeric data. Defaults to False.

    Returns:
        ft.DataColumn: The created data column.
    """
    return ft.DataColumn(
        label=ft.Text(value=label, color='blue'),
        tooltip=f'Ordenar por {label.lower()}',
        on_sort=on_sort,
    )


def create_data_cell(value: str) -> ft.DataCell:
    """
    Creates a data cell for the inventory table view.

    Args:
        value (str): The value to be displayed in the data cell.
        is_numeric (bool, optional): Specifies whether the value is numeric or not. Defaults to False.

    Returns:
        ft.DataCell: The created data cell.

    """
    def enable_txt_field(e):
        """
        Enables or disables the text field for editing.

        Args:
            e (ft.Event): The event object.

        """
        txt_field.read_only = not txt_field.read_only
        txt_field.focus()
        e.control.update()

    txt_field = ft.TextField(
        value=value,
        expand=True,
        read_only=True,
        border=ft.InputBorder.NONE,
    )

    return ft.DataCell(
        content=txt_field,
        # on_tap=enable_txt_field,
    )


def create_row(*product_attributes) -> ft.DataRow:
    """
    Creates a data row for the inventory table.

    Args:
        *product_attributes: Variable number of product attributes.

    Returns:
        ft.DataRow: The created data row.

    Raises:
        ValueError: If the number of attributes does not match the number of columns.
    """
    if len(product_attributes) != len(ProductAttributes):
        raise ValueError('The number of attributes does not match the number of columns')
    return ft.DataRow(
        cells=[
            create_data_cell(
                value=attr_value,
            ) for attr_value in product_attributes
        ]
    )


column_to_attribute_map = {
    col_name.value: prod_attr.value
    for col_name, prod_attr
    in zip(ColumnNames, ProductAttributes)
}

columns_state_order = {
    name.value: True 
    for name 
    in ColumnNames
}


class ProductTable(ft.DataTable):

    def __init__(self, products):
        super().__init__()
        self._products = products
        self.columns = [
            create_column(
                on_sort=self.sort_products,
                label=column_name.value,
            ) for column_name in ColumnNames
        ]
        self.rows = [
            create_row(
                product.unit,
                product.category,
                product.brand,
                product.quantity,
                product.cost_price,
                product.selling_price,
                product.reorder_level,
            ) for product in self.products
        ]
    
    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products: List):
        self._products = products
    
    def sort_products(self, event):
        col_name = event.control.label.value
        attr_name = column_to_attribute_map[col_name]
        columns_state_order[col_name] = not columns_state_order[col_name]
        self._products.sort(
            key=lambda product: getattr(product, attr_name),
            reverse=columns_state_order[col_name]
        )
        self.update_table()
    
    def update_table(self):
        self.rows = [
            create_row(
                product.unit,
                product.category,
                product.brand,
                product.quantity,
                product.cost_price,
                product.selling_price,
                product.reorder_level,
            ) for product in self.products
        ]
        self.update()
