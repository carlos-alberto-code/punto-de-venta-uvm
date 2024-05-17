import sys
sys.path.append('app/')

from attr import attrib
import flet as ft

from ProductTable import ProductTable, create_column, create_data_cell
from database.models import Product, Unit, Category, Brand
from controllers.products_controller import ProductController

controller = ProductController()
products = controller.get_all()

column_names = ('UNIDAD', 'CATEGORIA', 'MARCA', 'CANTIDAD', 'PRECIO DE COMPRA', 'PRECIO DE VENTA', 'Nivel de reorden')
attribute_names = ('unit', 'category', 'brand', 'quantity', 'cost_price', 'selling_price', 'reorder_level')

column_to_attribute_map = dict(zip(column_names, attribute_names))
columns_state_order = {name: True for name in column_names}

def sort_products(event):
    global last_sort_column
    column_name = event.control.label.value
    attribute_name = column_to_attribute_map[column_name]
    columns_state_order[column_name] = not columns_state_order[column_name]
    products.sort(key=lambda p: getattr(p, attribute_name), reverse=columns_state_order[column_name])
    product_table.rows = [
        ft.DataRow(
            cells=[create_data_cell(getattr(product, prop)) for prop in attribute_names]
        ) for product in products
    ]
    product_table.sort_ascending = columns_state_order[column_name]
    product_table.update()
 
colums = [
    create_column(label=prop, on_sort=sort_products) for prop in columns_state_order
]

rows = [
    ft.DataRow(
        cells=[
            create_data_cell(getattr(product, prop)) for prop in attribute_names
        ]
    ) for product in products

]
product_table = ProductTable(
    columns=colums,
    rows=rows
)

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.add(product_table)
    page.on_scroll = lambda e: print(e.scroll_y)

ft.app(target=main)