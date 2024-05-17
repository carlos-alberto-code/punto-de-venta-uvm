import flet as ft
from time import sleep
from attr import dataclass
from typing import Callable, Optional, List

from numpy import product


@dataclass
class ColumnNames:
    """
    Represents the column names for the inventory table view.
    """

    unit:          str = 'UNIDAD'
    category:      str = 'CATEGORIA'
    brand:         str = 'MARCA'
    quantity:      str = 'CANTIDAD'
    cost_price:    str = 'PRECIO DE COMPRA'
    selling_price: str = 'PRECIO DE VENTA'
    reorder_level: str = 'NIVEL DE REORDEN'

    def __iter__(self):
        yield from self.__dict__.values()


@dataclass
class ProductAttributes:
    """
    Represents the attributes of a product.

    Attributes:
        unit (str): The unit of measurement for the product.
        category (str): The category of the product.
        brand (str): The brand of the product.
        quantity (str): The quantity of the product.
        cost_price (str): The cost price of the product.
        selling_price (str): The selling price of the product.
        reorder_level (str): The reorder level of the product.
    """

    unit: str = 'unit'
    category: str = 'category'
    brand: str = 'brand'
    quantity: str = 'quantity'
    cost_price: str = 'cost_price'
    selling_price: str = 'selling_price'
    reorder_level: str = 'reorder_level'

    def __iter__(self):
        yield from self.__dict__.values()
    
    def __len__(self):
        return len(self.__dict__)


@dataclass
class ProductAttributesTypes:
    """
    Represents the attribute types for a product.

    Attributes:
        unit (type): The unit of measurement for the product.
        category (type): The category of the product.
        brand (type): The brand of the product.
        quantity (type): The quantity of the product.
        cost_price (type): The cost price of the product.
        selling_price (type): The selling price of the product.
        reorder_level (type): The reorder level of the product.
    """

    unit:          type = str
    category:      type = str
    brand:         type = str
    quantity:      type = int
    cost_price:    type = float
    selling_price: type = float
    reorder_level: type = int

    def __iter__(self):
        yield from self.__dict__.values()


def create_column(label: str, on_sort: Optional[Callable] = None, is_numeric=False) -> ft.DataColumn:
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
        label=ft.Text(value=label),
        tooltip=f'Ordenar por {label.lower()}',
        on_sort=on_sort,
        numeric=is_numeric
    )


def create_data_cell(value: str, is_numeric=False) -> ft.DataCell:
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
        input_filter=ft.NumbersOnlyInputFilter() if is_numeric else ft.TextOnlyInputFilter(),
    )

    return ft.DataCell(
        content=txt_field,
        on_tap=enable_txt_field,
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
    if len(product_attributes) != len(ProductAttributes()):
        raise ValueError('The number of attributes does not match the number of columns')
    return ft.DataRow(
        cells=[
            create_data_cell(
                value=attr_value,
                is_numeric=issubclass(attr_type, (float, int))
            ) for attr_value, attr_type in zip(
            product_attributes, ProductAttributesTypes()
            )
        ]
    )


column_to_attribute_map = dict(zip(ColumnNames(), ProductAttributes()))
columns_state_order = {name: True for name in ColumnNames()}


class ProductTable(ft.DataTable):

    def __init__(self, products):
        super().__init__()
        self._products = products
        self.columns = [
            create_column(
                on_sort=self.sort_products,
                label=column_name,
                is_numeric=issubclass(column_type, (float, int))
            ) for column_name, column_type in zip(ColumnNames(), ProductAttributesTypes())
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
        self.columns = [
            create_column(
                on_sort=self.sort_products,
                label=column_name,
                is_numeric=issubclass(column_type, (float, int))
            ) for column_name, column_type in zip(ColumnNames(), ProductAttributesTypes())
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
        self.update()