import flet as ft
from enum import Enum


class Column(Enum):
    UNIT = ('UNIDAD', 'unit')
    CATEGORY = ('CATEGORIA', 'category')
    BRAND = ('MARCA', 'brand')
    QUANTITY = ('CANTIDAD', 'quantity')
    COST_PRICE = ('PRECIO DE COMPRA', 'cost_price')
    SELLING_PRICE = ('PRECIO DE VENTA', 'selling_price')
    REORDER_LEVEL = ('NIVEL DE REORDEN', 'reorder_level')


class ProductTable(ft.DataTable):

    def __init__(self, products: list):
        super().__init__(
            columns=[
                self._create_data_column(
                    label=column.value[0],
                    on_click=self.sort_products
                ) for column in Column
            ],
            border=ft.border.all(width=1, color=ft.colors.GREY_300),
            border_radius=15,
        )
        self._products = products
        self.column_state_order = {column.value[0]: True for column in Column}
        self.column_to_attribute_map = {column.value[0]: column.value[1] for column in Column}
        self.update_table()

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products: list):
        self._products = products
        self.update_table()
        self.update()

    def _create_data_cell(self, value: str):
        return ft.DataCell(ft.Text(value=value), on_tap=self.handle_on_tap_cell)

    def handle_on_tap_cell(self, event: ft.ControlEvent):
        self.convert_to_text_field(event)

    def convert_to_text_field(self, event: ft.ControlEvent):
        self.selected_cell = event.control
        self.update_cell_content(ft.TextField(label='Modifica', autofocus=True, on_submit=self.convert_to_text))

    def convert_to_text(self, event: ft.ControlEvent):
        self.selected_txt_field = event.control
        self.update_cell_content(ft.Text(value=self.selected_txt_field.value))

    def update_cell_content(self, new_content):
        self.selected_cell.content = new_content
        self.selected_cell.update()

    def _create_data_row(self, product):
        return ft.DataRow(
            cells=[
                self._create_data_cell(value=getattr(product, column.value[1]))
                for column in Column
            ]
        )

    def _create_data_column(self, label: str, on_click):
        return ft.DataColumn(
            label=ft.Text(value=label.capitalize(), color='blue'),
            tooltip=f'Ordenar por {label.lower()}',
            on_sort=on_click,
        )

    def update_table(self):
        self.rows = [self._create_data_row(product) for product in self._products]

    def sort_products(self, event):
        column_name = event.control.label.value.upper()
        attr_name = self.column_to_attribute_map[column_name]
        self.column_state_order[column_name] = not self.column_state_order[column_name]
        self._products.sort(
            key=lambda product: getattr(product, attr_name),
            reverse=self.column_state_order[column_name]
        )
        self.update_table()
        self.update()
        