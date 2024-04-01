from ..navigation.builder import Module, Section
from .content.purchases.suppliers_section import content


import flet as ft


Module(
    'Compras',
    ft.icons.SHOPPING_BASKET,
    Section('Proveedores', ft.icons.ABC, content)
)