from ..navigation.builder import Module, Section
from .content.inventory.stock_section import StockSection
# from .content.inventory.reports_section import PurchaseSection
import flet as ft


Module(
    'Inventario',
    ft.icons.ADD_BOX,
    Section(name='Stock', icon=ft.icons.STORAGE, content=StockSection),
    Section(name='Reportes', icon=ft.icons.INSERT_CHART),
)