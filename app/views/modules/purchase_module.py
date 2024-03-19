from navigation_structure import Module, Section
import flet as ft


Purchase = Module(
    'Compras',
    ft.icons.SHOP,
    Section('Compras', ft.icons.SHOPPING_CART),
    Section('Inventario', ft.icons.INVENTORY),
    Section('Proveedores', ft.icons.PEOPLE),
)