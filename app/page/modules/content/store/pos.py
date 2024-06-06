# Componentes del punto de venta
# - Búsqueda de productos
# - Tabla de productos
# - Carrito de compras
# - Controles de ajuste

import flet as ft
from page.modules.content.store.product_searcher_behavior import SearchBarHandler
from controllers.controllers import ProductController

product_controller = ProductController()
product_table = ft.DataTable()

handler = SearchBarHandler(controller=product_controller, table=product_table)

product_Searcher = ft.SearchBar(
    height=40,
    bar_hint_text='Buscar producto',
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    autofocus=True,
    on_tap=handler.on_tap,
    on_change=handler.on_change,
)