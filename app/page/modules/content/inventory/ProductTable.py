import flet as ft
from typing import Callable, Optional, List
from controllers.products_controller import ProductController


def create_column(label: str, on_sort: Optional[Callable] = None):
    return ft.DataColumn(
        label=ft.Text(value=label),
        on_sort=on_sort,
    )





def create_data_cell(value: str) -> ft.DataCell:
    def eneable_txt_field(e):
        txt_field.read_only = False
        txt_field.focus()
        e.control.update()

    txt_field = ft.TextField(
        value=value,
        expand=True,
        read_only=True,
        border=ft.InputBorder.NONE
    )
    return ft.DataCell(
        content=txt_field,
        on_tap=eneable_txt_field
    )


class ProductTable(ft.DataTable):

    def __init__(self, columns: Optional[List[ft.DataColumn]] = None, rows: Optional[List[ft.DataRow]] = None):
        super().__init__(
            columns=columns,
            rows=rows,
            border_radius=10,
        )
