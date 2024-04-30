from ..navigation.module import Module, Section
from .content.inventory.stock_section import StockSection
# from .content.inventory.reports_section import PurchaseSection
import flet as ft


Module(
    'Inventario',
    ft.icons.ADD_BOX,
    Section(label='Stock', icon=ft.icons.STORAGE, content=StockSection()),
    Section(label='Reportes', icon=ft.icons.INSERT_CHART),
)