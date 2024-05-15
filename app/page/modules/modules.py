import flet as ft
from page.navigation.module import Module, Section


# SECCIONES DEL MÓDULO DE COMPRAS

from .content.purchases.purchase_section   import PurchaseSection
from .content.purchases.suppliers_section  import ProvidersSection
from .content.purchases.categories_section import CategoriesSection

Module(
    'Compras',
    ft.icons.SHOPPING_BASKET,
    Section('Entradas',ft.icons.LIBRARY_ADD_CHECK_ROUNDED,PurchaseSection),
    Section('Proveedores',ft.icons.PERSON_PIN_ROUNDED,ProvidersSection),
    Section('Categorias',ft.icons.CHECKLIST_ROUNDED,CategoriesSection),
)


# SECCIONES DEL MÓDULO DE INVENTARIO

from .content.inventory.stock_section    import StockSection
from .content.inventory.TestStockSection import TestStockSection

Module(
    'Inventario',
    ft.icons.STORAGE,
    Section(
        label='Stock',
        icon=ft.icons.ADD_BOX,
        content=StockSection()
    ),
    Section(
        label='Test Stock Section',
        icon=ft.icons.ADD_BOX,
        content=TestStockSection()
    ),
)

# OTROS MÓDULOS...
