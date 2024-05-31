# NOTE: La forma en la que se declaren los módulos y secciones, es el orden en que aparecerán.

import flet as ft
from page.navigation.module import Module, Section


# SECCIONES DEL MÓDULO DE COMPRAS

from page.modules.content.purchases.purchase_section   import PurchaseSection
from page.modules.content.purchases.suppliers_section  import ProvidersSection
from page.modules.content.purchases.categories_section import CategoriesSection

Module(
    'Compras',
    ft.icons.SHOPPING_BASKET,
    Section('Entradas',ft.icons.LIBRARY_ADD_CHECK_ROUNDED,PurchaseSection),
    Section('Proveedores',ft.icons.PERSON_PIN_ROUNDED,ProvidersSection),
    Section('Categorias',ft.icons.CHECKLIST_ROUNDED,CategoriesSection),
)


# SECCIONES DEL MÓDULO DE INVENTARIO

from page.modules.content.inventory.stock_section import StockSection

Module(
    'Inventario', ft.icons.STORAGE, Section('Stock', ft.icons.ADD_BOX, StockSection()),
)

# OTROS MÓDULOS...
