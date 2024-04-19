import flet as ft
import sys
sys.path.append('..')
from controllers.categories_controller import CategorieController

_title = ft.Text('Categorias',size=25)
_table = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('NOMBRE'))
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(categorie.id))),
                ft.DataCell(ft.Text(categorie.name))
            ]
        )for categorie in CategorieController().get_all()
    ]
)

CategoriesSection = ft.Column(
    scroll=ft.ScrollMode.ALWAYS,
    controls=[
        ft.Row(
            [
                ft.Icon(name=ft.icons.CHECKLIST_ROUNDED),
                _title
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [_table],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ]
)