from time import sleep
import sys
sys.path.append('app/')

import flet as ft

# from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
# from ProductTable import create_column, create_row, create_data_cell, sort_products, columns_state_order, attribute_names
from controllers.products_controller import ProductController
from ProductTable import ProductTable

controller = ProductController()
products = controller.get_all()[:30]

product_table = ProductTable(products)

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.add(product_table)

ft.app(target=main)