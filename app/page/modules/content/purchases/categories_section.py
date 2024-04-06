import flet as ft

_title = ft.Text('Categorias',size=25)
_table = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('NOMBRE'))
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('1')),
                ft.DataCell(ft.Text('Electronicos'))
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('2')),
                ft.DataCell(ft.Text('Ropa'))
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('3')),
                ft.DataCell(ft.Text('Alimentos'))
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('4')),
                ft.DataCell(ft.Text('Hogar'))
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('5')),
                ft.DataCell(ft.Text('Tecnologia'))
            ]
        ),
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text('6')),
                ft.DataCell(ft.Text('Zapatos'))
            ]
        ),
    ]
)

CategoriesSection = ft.Column(
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