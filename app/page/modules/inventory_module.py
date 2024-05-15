import flet as ft
from ..navigation.module import Module, Section
from .content.inventory.stock_section import StockSection


Module(
    'Inventario',
    ft.icons.STORAGE,
    Section(
        label='Stock',
        icon=ft.icons.ADD_BOX,
        content=StockSection()
    ),
)