from navigation_structure import Module, Section
import flet as ft



def create_modules():

    Sales = Module(
        'Ventas',
        ft.icons.SHOP,
        Section('Ventas', ft.icons.SHOPPING_CART),
        # La creación de secciones del módulo de ventas sigue este patrón
    )

    print(Sales)

    Purchase = Module(
        'Compras',
        ft.icons.SHOP,
        Section('Compras', ft.icons.SHOPPING_CART),
        # La creación de secciones del módulo de compras sigue este patrón
    )


create_modules() # This is the function that is being called in app/main.py