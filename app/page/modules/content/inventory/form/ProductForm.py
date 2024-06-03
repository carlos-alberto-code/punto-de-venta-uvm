from typing import Optional
import flet as ft

from page.components.counters import Counter

from page.modules.content.inventory.searchers import SimpleModelSearcher as Searcher
from controllers.controllers import UnitController, CategoryController, BrandController
from interfaces.interfaces import FieldInterface


ft.AlertDialog()
class ProductForm(ft.AlertDialog):

    def __init__(
            self,
            *fields: FieldInterface,
            actions: list[ft.Control] = [],
    ):
        super().__init__(
            title=ft.Text('Nuevo producto'),
            icon=ft.Icon(str(ft.icons.INVENTORY)),
            scrollable=True,
        )
        self.content = ft.Column(
            controls=[
                Searcher(UnitController()),
                Searcher(CategoryController()),
                Searcher(BrandController()),
                ft.Row(
                    [
                        ft.Text('Cantidad:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Text('Precio de compra:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Text('Precio de venta:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Text('Existencias mínimas:'),
                        Counter(start_value=1),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ],
        )
        self.actions = actions


ft.AlertDialog()
class Form(ft.AlertDialog):

    def __init__(
            self,
            title: Optional[str] = None,
            icon: Optional[str] = None,
            actions: list[ft.Control] = [],
            *fields: FieldInterface,
    ):
        super().__init__(
            title=ft.Row([ft.Text(value=title)], alignment=ft.MainAxisAlignment.CENTER),
            icon=ft.Icon(name=icon),
            scrollable=True,
            actions=actions,
            actions_alignment=ft.MainAxisAlignment.END,
        )
        if fields:
            for field in fields:
                print(field.value)
