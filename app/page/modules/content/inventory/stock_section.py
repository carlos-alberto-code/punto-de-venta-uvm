import flet as ft
from controllers.inventory_controller import InventoryController

# Carlos: Implementación
from controllers.products_controller import ProductController

_title = ft.Text('Inventario', size=25)
_table = ft.DataTable(
    sort_column_index=0,
    sort_ascending=False,
    columns=[
        ft.DataColumn(ft.Text('sku')),
        ft.DataColumn(ft.Text('Unidad ID')),
        ft.DataColumn(ft.Text('Categoria ID')),
        ft.DataColumn(ft.Text('Marca ID')),
        ft.DataColumn(ft.Text('Cantidad')),
        ft.DataColumn(ft.Text('Precio de compra')),
        ft.DataColumn(ft.Text('Precio de venta')),
        ft.DataColumn(ft.Text('Stock minimo')),
        ft.DataColumn(ft.Text('Descripcion')),
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(product.sku))),
                ft.DataCell(ft.Text(str(product.unit_id))),
                ft.DataCell(ft.Text(str(product.category_id))),
                ft.DataCell(ft.Text(str(product.brand_id))),
                ft.DataCell(ft.Text(str(product.quantity))),
                ft.DataCell(ft.Text(str(product.purchase_price))),
                ft.DataCell(ft.Text(str(product.sale_price))),
                ft.DataCell(ft.Text(str(product.minimum_stock))),
                ft.DataCell(ft.Text(product.description)),
            ]
        )for product in InventoryController().get_all()
    ]
)

stock_section = ft.Column(
    scroll=ft.ScrollMode.ALWAYS,
    controls=[
        ft.Row(
            [
                ft.Icon(name=ft.icons.INVENTORY),
                _title
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [_table],
            alignment=ft.MainAxisAlignment.CENTER
        )
    ]
)

# Carlos: Implementación


_search_bar = ft.TextField(
    label='Buscar',
)

_filter_by = ft.Dropdown(
    label='Filtrar por',
    options=[
        ft.dropdown.Option(text='Categoría'),
        ft.dropdown.Option(text='Unidad'),
        ft.dropdown.Option(text='Marca'),
    ]
)


class StockSection(ft.Column):
    
    def __init__(self):
        super().__init__()
        self.products = ProductController.get_all()
        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    _search_bar,
                    _filter_by
                ],
            ), # Row End
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.TextButton('SKU')),
                    ft.DataColumn(ft.TextButton('UNIDAD')),
                    ft.DataColumn(ft.TextButton('CATEGORÍA')),
                    ft.DataColumn(ft.TextButton('MARCA')),
                    ft.DataColumn(ft.TextButton('CANTIDAD')),
                    ft.DataColumn(ft.TextButton('PRECIO DE COMPRA')),
                    ft.DataColumn(ft.TextButton('PRECIO DE VENTA')),
                    ft.DataColumn(ft.TextButton('STOCK MÍNIMO')),
                    ft.DataColumn(ft.TextButton('DESCRIPCIÓN')),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(product.sku))),
                            ft.DataCell(ft.Text(str(product.unit))),
                            ft.DataCell(ft.Text(str(product.category))),
                            ft.DataCell(ft.Text(str(product.brand))),
                            ft.DataCell(ft.Text(str(product.quantity))),
                            ft.DataCell(ft.Text(str(product.purchase_price))),
                            ft.DataCell(ft.Text(str(product.sale_price))),
                            ft.DataCell(ft.Text(str(product.minimum_stock))),
                            ft.DataCell(ft.Text(product.description)),
                        ]
                    ) for product in self.products
                    
                ]
            )
        ]