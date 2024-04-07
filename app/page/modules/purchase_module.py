from ..navigation.builder import Module, Section
from .content.purchases.suppliers_section import ProvidersSection
from .content.purchases.purchase_section import PurchaseSection
from .content.purchases.categories_section import CategoriesSection


import flet as ft


Module(
    'Compras',
    ft.icons.SHOPPING_BASKET,
    Section('Entradas',ft.icons.LIBRARY_ADD_CHECK_ROUNDED,PurchaseSection),
    Section('Proveedores',ft.icons.PERSON_PIN_ROUNDED,ProvidersSection),
    Section('Categorias',ft.icons.CHECKLIST_ROUNDED,CategoriesSection),
)