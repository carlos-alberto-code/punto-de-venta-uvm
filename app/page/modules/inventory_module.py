from ..navigation.builder import Module, Section
from .content.inventory.inventory_section import InventorySection
from .content.inventory.purchase_section import PurchaseSection
import flet as ft


Module(
    'Inventario',
    ft.icons.ADD_BOX,
    Section("Inventario",ft.icons.INVENTORY,InventorySection),
    Section("Entradas (Compras)",ft.icons.LIBRARY_ADD_CHECK_ROUNDED,PurchaseSection)
)