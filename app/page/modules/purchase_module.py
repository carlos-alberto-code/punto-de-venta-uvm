from ..navigation.builder import Module, Section
from .content.purchases.suppliers_section import content
from .content.purchases.purchase_section import PurchaseSection


import flet as ft


Module(
    'Compras',
    ft.icons.SHOPPING_BASKET,
    #Section('Proveedores', ft.icons.ABC, content),
    Section('Entradas',ft.icons.LIBRARY_ADD_CHECK_ROUNDED,PurchaseSection)
)