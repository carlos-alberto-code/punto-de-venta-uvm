import sys
sys.path.append('app/')

import flet as ft

# from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
# from ProductTable import create_column, create_row, create_data_cell, sort_products, columns_state_order, attribute_names
from controllers.products_controller import ProductController
from table_view import (
    ColumnNames,
    ProductAttributes,
    ProductAttributesTypes,
    sort_products,
    create_column,
    create_row,
)

controller = ProductController()
products = controller.get_all()[:30]

product_table = ft.DataTable(
    columns=[
        create_column(
            label=col_name,
            is_numeric=issubclass(col_type, (float, int)),
            on_sort=sort_products
        ) for col_name, col_type in zip(ColumnNames(), ProductAttributesTypes()
        )
    ],
    rows=[
        create_row(
            product.unit,
            product.category,
            product.brand,
            product.quantity,
            product.cost_price,
            product.selling_price,
            product.reorder_level,
        ) for product in products
    ],
    vertical_lines=ft.BorderSide(width=1),
    horizontal_lines=ft.BorderSide(width=1),
    border_radius=10,
    border=ft.border.all(1),
)

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.add(product_table)

ft.app(target=main)