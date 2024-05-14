import flet as ft

from controllers.products_controller import ProductController
from page.components.search_bar_filter.SearchBarFilter import SearchBarFilter
from page.modules.content.inventory.top_buttons import AddNewButton, ShareButton
from page.components.search_bar_filter.properties_controller import UnitFilter, CategoryFilter, BrandFilter


_search_bar = SearchBarFilter(
    Categoria=CategoryFilter(),
    Marca=BrandFilter(),
    Unidad=UnitFilter(),
)

_filter_by = ft.Dropdown(
    label='Filtrar por',
    options=[
        ft.dropdown.Option(text='Categoría'),
        ft.dropdown.Option(text='Unidad'),
        ft.dropdown.Option(text='Marca'),
    ]
)
top = ft.Row(
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    controls=[
        _search_bar,
        ft.Row(
            controls=[
                ShareButton(),
                AddNewButton(),
            ]
        )
    ]
)

class StockSection(ft.Column):
    
    def __init__(self):
        super().__init__()
        self.products = ProductController().get_all_products()
        self.spacing = 20
        self.sort_functions = {
            # 'sku': lambda: self.sort_by('sku', int),
            'unit': lambda: self.sort_by('unit', lambda x: str(x).lower()),
            'category': lambda: self.sort_by('category', lambda x: str(x).lower()),
            'brand': lambda: self.sort_by('brand', lambda x: str(x).lower()),
            'quantity': lambda: self.sort_by('quantity', int),
            'cost_price': lambda: self.sort_by('cost_price', float),
            'selling_price': lambda: self.sort_by('selling_price', float),
            'reorder_leve': lambda: self.sort_by('reorder_leve', int),
        }
        self.sort_order = {key: True for key in self.sort_functions.keys()}
        self.controls = [
            top,
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.TextButton('SKU', on_click=lambda event: self.sort_by_key('sku', event)), visible=False),
                    ft.DataColumn(ft.TextButton('UNIDAD', on_click=lambda event: self.sort_by_key('unit', event))),
                    ft.DataColumn(ft.TextButton('CATEGORÍA', on_click=lambda event: self.sort_by_key('category', event))),
                    ft.DataColumn(ft.TextButton('MARCA', on_click=lambda event: self.sort_by_key('brand', event))),
                    ft.DataColumn(ft.TextButton('CANTIDAD', on_click=lambda event: self.sort_by_key('quantity', event))),
                    ft.DataColumn(ft.TextButton('PRECIO DE COMPRA', on_click=lambda event: self.sort_by_key('cost_price', event))),
                    ft.DataColumn(ft.TextButton('PRECIO DE VENTA', on_click=lambda event: self.sort_by_key('selling_price', event))),
                    ft.DataColumn(ft.TextButton('STOCK MÍNIMO', on_click=lambda event: self.sort_by_key('reorder_leve', event))),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(product.sku)), visible=False),
                            ft.DataCell(ft.Text(str(product.unit))),
                            ft.DataCell(ft.Text(str(product.category))),
                            ft.DataCell(ft.Text(str(product.brand))),
                            ft.DataCell(ft.Text(str(product.quantity)), on_tap=lambda e: print(e.control.content)),
                            ft.DataCell(ft.Text(str(product.cost_price))),
                            ft.DataCell(ft.Text(str(product.selling_price))),
                            ft.DataCell(ft.Text(str(product.reorder_level))),
                        ],
                        # selected=True,
                        # on_select_changed=lambda e: print(f"row select changed: {e.control.cells[2].content}"),
                    ) for product in self.products
                    
                ]
            )
        ]

    def sort_by(self, attribute, type):
        reverse_order = not self.sort_order[attribute]
        self.products = sorted(self.products, key=lambda product: type(getattr(product, attribute)), reverse=reverse_order)
        self.sort_order[attribute] = reverse_order
        self.update_table()

    def update_table(self):
        self.controls[1].rows = [ # type: ignore
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(product.sku))),
                    ft.DataCell(ft.Text(str(product.unit))),
                    ft.DataCell(ft.Text(str(product.category)), on_tap=lambda e: print(e.control)),
                    ft.DataCell(ft.Text(str(product.brand)), show_edit_icon=True),
                    ft.DataCell(ft.Text(str(product.quantity))),
                    ft.DataCell(ft.Text(str(product.cost_price))),
                    ft.DataCell(ft.Text(str(product.selling_price))),
                    ft.DataCell(ft.Text(str(product.reorder_level)), on_tap=lambda e: print('tap'), on_double_tap=lambda e: print('Duble tap', e.control)),
                ],
                selected=True,
                on_select_changed=lambda e: print(e.control),
            ) for product in self.products
        ]
    
    def sort_by_key(self, key: str, event: ft.ControlEvent):
        self.sort_functions[key]()
        self.update()

