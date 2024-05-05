import flet as ft

from controllers.products_controller import ProductController


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
        self.products = ProductController.get_all_products()
        self.spacing = 20
        self.sort_functions = {
            'sku': lambda: self.sort_by('sku', int),
            'unit': lambda: self.sort_by('unit', lambda x: str(x).lower()),
            'category': lambda: self.sort_by('category', lambda x: str(x).lower()),
            'brand': lambda: self.sort_by('brand', lambda x: str(x).lower()),
            'quantity': lambda: self.sort_by('quantity', int),
            'purchase_price': lambda: self.sort_by('purchase_price', float),
            'sale_price': lambda: self.sort_by('sale_price', float),
            'minimum_stock': lambda: self.sort_by('minimum_stock', int),
        }
        self.sort_order = {key: True for key in self.sort_functions.keys()}
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
                    ft.DataColumn(ft.TextButton('SKU', on_click=lambda event: self.sort_by_key('sku', event))),
                    ft.DataColumn(ft.TextButton('UNIDAD', on_click=lambda event: self.sort_by_key('unit', event))),
                    ft.DataColumn(ft.TextButton('CATEGORÍA', on_click=lambda event: self.sort_by_key('category', event))),
                    ft.DataColumn(ft.TextButton('MARCA', on_click=lambda event: self.sort_by_key('brand', event))),
                    ft.DataColumn(ft.TextButton('CANTIDAD', on_click=lambda event: self.sort_by_key('quantity', event))),
                    ft.DataColumn(ft.TextButton('PRECIO DE COMPRA', on_click=lambda event: self.sort_by_key('purchase_price', event))),
                    ft.DataColumn(ft.TextButton('PRECIO DE VENTA', on_click=lambda event: self.sort_by_key('sale_price', event))),
                    ft.DataColumn(ft.TextButton('STOCK MÍNIMO', on_click=lambda event: self.sort_by_key('minimum_stock', event))),
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
                        ],
                        selected=True,
                        on_select_changed=lambda event: print(event),
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
                    ft.DataCell(ft.Text(str(product.category))),
                    ft.DataCell(ft.Text(str(product.brand))),
                    ft.DataCell(ft.Text(str(product.quantity))),
                    ft.DataCell(ft.Text(str(product.purchase_price))),
                    ft.DataCell(ft.Text(str(product.sale_price))),
                    ft.DataCell(ft.Text(str(product.minimum_stock))),
                    ft.DataCell(ft.Text(product.description)),
                ],
                selected=True,
                on_select_changed=lambda e: print(type(e)),
            ) for product in self.products
        ]
    
    def sort_by_key(self, key: str, event: ft.ControlEvent):
        self.sort_functions[key]()
        self.update()

from time import sleep
ft.SearchBar()
class Filter(ft.SearchBar):
    # Esta clase es un componente de búsqueda y filtrado, pensado para buscar y filtrar en función de las unidades, categorías y marcas
    def __init__(self):
        super().__init__()
        self.width = 400
        self.height = 40
        self.tooltip = 'Selecciona un filtro y escribe el nombre de la unidad, categoría o marca que deseas buscar'
        self.bar_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.view_leading = ft.Icon(name=ft.icons.SEARCH_SHARP)
        self.bar_hint_text = 'Selecciona un filtro'
        self.bar_trailing = [
            ft.PopupMenuButton(
                icon=ft.icons.FILTER_LIST,
                items=[
                    ft.PopupMenuItem(text='Unidad', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Categoría', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Marca', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                ]
            )
        ]
        self.view_trailing = [
            ft.PopupMenuButton(
                icon=ft.icons.FILTER_LIST,
                items=[
                    ft.PopupMenuItem(text='Unidad', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Categoría', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                    ft.PopupMenuItem(text='Marca', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE, on_click=self.run_searcher),
                ]
            ),
            ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view()),
        ]
        self.on_tap = self.do_nothing
        # Siempre debe ir un control al final que permita agregar una nueva propiedad, dependiendo del filtro seleccionado
        # Al seleccionarse un filtro, se inyectan los controles dependiendo la opción seleccionada.
        # Pero siempre estará el control para registrar una nueva propiedad al final de las opciones.
        self.controls = [ft.ElevatedButton(text='Agregar nueva propiedad', icon=ft.icons.ADD)]
    
    def do_nothing(self, event):
        self.close_view()
    
    def run_searcher(self, event):
        self.view_hint_text = f'Escribe el nombre de la {event.control.text.lower()}'
        self.close_view()
        sleep(0.08)
        self.open_view()
