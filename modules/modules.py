import flet as ft

from naveasey.naveasey                   import Module
from modules.purchase_view.context       import shape
from modules.store_view.context          import StoreShape
from modules.inventory_view.view_section import ContentStockSectionShape
from modules.suppliers_view.view_section import ContentStockSectionShape as SupplierContent


Module(
    name='Tienda',
    icon=ft.icons.POINT_OF_SALE,
    content=StoreShape
)

Module(
    name='Productos',
    icon=ft.icons.INVENTORY,
    content=ContentStockSectionShape()
)

Module(
    name='Compras',
    icon=ft.icons.SHOPPING_CART,
    content=shape
)

Module(
    name='Proveedores',
    icon=ft.icons.PEOPLE,
    content=SupplierContent()
)
