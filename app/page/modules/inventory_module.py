import flet as ft
from ..navigation.module import Module, Section
from .content.inventory.stock_section import StockSection
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