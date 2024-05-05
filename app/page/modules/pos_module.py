from ..navigation.module import Module, Section
import flet as ft
from .content.sellPoint.sales_section import SalesSection

Module(
    'Punto de venta',
    ft.icons.SHOP,
    Section('Ventas',ft.icons.SHOPPING_BAG,content=SalesSection())
)