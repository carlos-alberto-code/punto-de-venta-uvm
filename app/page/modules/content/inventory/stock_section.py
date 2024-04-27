import flet as ft
from controllers.inventory_controller import InventoryController

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

StockSection = ft.Column(
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
    