import flet as ft
from attr import dataclass
from typing import Optional, Callable


@dataclass
class ColumnNames:
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
    unit:          str = 'unit'
    category:      str = 'category'
    brand:         str = 'brand'
    quantity:      str = 'quantity'
    cost_price:    str = 'cost_price'
    selling_price: str = 'selling_price'
    reorder_level: str = 'reorder_level'

    def __iter__(self):
        yield from self.__dict__.values()
    
    def __len__(self):
        return len(self.__dict__)


@dataclass
class ProductAttributesTypes:
    unit:          type = str
    category:      type = str
    brand:         type = str
    quantity:      type = int
    cost_price:    type = float
    selling_price: type = float
    reorder_level: type = int

    def __iter__(self):
        yield from self.__dict__.values()


column_to_attribute_map = dict(zip(ColumnNames(), ProductAttributes()))
columns_state_order = {name: True for name in ColumnNames()}


def create_column(label: str, on_sort: Optional[Callable] = None, is_numeric=False) -> ft.DataColumn:
    return ft.DataColumn(
        label=ft.Text(value=label),
        tooltip=f'Ordenar por {label.lower()}',
        on_sort=on_sort,
        numeric=is_numeric
    )


def _create_data_cell(value: str, is_numeric=False) -> ft.DataCell:
    
        def enable_txt_field(e):
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
    if len(product_attributes) != len(ProductAttributes()):
        raise ValueError('The number of attributes does not match the number of columns')
    return ft.DataRow(
        cells=[
            _create_data_cell(
                value=attr_value,
                is_numeric=issubclass(attr_type, (float, int))
            ) for attr_value, attr_type in zip(
            product_attributes, ProductAttributesTypes()
            )
        ]
    )