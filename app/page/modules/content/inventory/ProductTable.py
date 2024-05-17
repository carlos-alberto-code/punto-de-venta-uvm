import flet as ft
from typing import Callable, Optional, List
from controllers.products_controller import ProductController


def create_column(label: str, on_sort: Optional[Callable] = None, is_numeric=False) -> ft.DataColumn:
    return ft.DataColumn(
        label=ft.Text(value=label),
        tooltip=f'Ordenar por {label}',
        on_sort=on_sort,
        numeric=is_numeric
    )





def create_data_cell(value: str, is_numeric=None) -> ft.DataCell:

    txt_field = ft.TextField(
        value=value,
        expand=True,
        read_only=True,
        border=ft.InputBorder.NONE,
        height=30,
        keyboard_type=ft.KeyboardType.NUMBER if is_numeric else ft.KeyboardType.TEXT,
    )

    def eneable_txt_field(e):
        txt_field.read_only = False
        txt_field.focus()
        e.control.update()

    return ft.DataCell(
        content=txt_field,
        on_tap=eneable_txt_field
    )


def create_row():
    pass


column_names = ('UNIDAD', 'CATEGORIA', 'MARCA', 'CANTIDAD', 'PRECIO DE COMPRA', 'PRECIO DE VENTA', 'Nivel de reorden')
attribute_names = ('unit', 'category', 'brand', 'quantity', 'cost_price', 'selling_price', 'reorder_level')
column_to_attribute_map = dict(zip(column_names, attribute_names))
columns_state_order = {name: True for name in column_names}

def sort_products(products, event):
    column_name = event.control.label.value
    attribute_name = column_to_attribute_map[column_name]
    columns_state_order[column_name] = not columns_state_order[column_name]
    products.sort(key=lambda product: getattr(product, attribute_name), reverse=columns_state_order[column_name])
    return [
        ft.DataRow(
            cells=[create_data_cell(getattr(product, prop)) for prop in attribute_names]
        ) for product in products
    ]
    product_table.sort_ascending = columns_state_order[column_name]
    product_table.update()