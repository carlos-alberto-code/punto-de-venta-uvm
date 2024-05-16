import sys
sys.path.append('app/')

import flet as ft
from ProductTable import ProductTable, create_column
from controllers.products_controller import ProductController

products = ProductController().get_all()
product_properties = ProductController().get_properties()

colums = [
    create_column(label=prop) for prop in product_properties
]
product_table = ProductTable(
    columns=colums,
)

def main(page: ft.Page):
    page.add(product_table)

ft.app(target=main)