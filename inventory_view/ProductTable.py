import flet as ft
from enum import Enum


class Column(Enum):
    UNIT          = ('UNIDAD', 'unit')
    CATEGORY      = ('CATEGORIA', 'category')
    BRAND         = ('MARCA', 'brand')
    QUANTITY      = ('CANTIDAD', 'quantity')
    COST_PRICE    = ('PRECIO DE COMPRA', 'cost_price')
    SELLING_PRICE = ('PRECIO DE VENTA', 'selling_price')
    REORDER_LEVEL = ('NIVEL DE REORDEN', 'reorder_level')


class ProductTable(ft.DataTable):

    def __init__(self, products: list):
        super().__init__(
            columns=[
                self.__create_data_column(
                    label=column.value[0],
                    on_click=self.__handle_on_sort_column
                ) for column in Column
            ],
            border=ft.border.all(width=1, color=ft.colors.GREY_300),
            border_radius=15,
        )
        self.__products = products
        self.__column_state_order = {column.value[0]: True for column in Column}
        self.__column_to_attribute_map = {column.value[0]: column.value[1] for column in Column}
        self.__update_table()

        self.__non_editable_columns = [Column.UNIT.value[0], Column.CATEGORY.value[0], Column.BRAND.value[0]]
        
    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products: list):
        self.__products = products
        self.__update_table()
        self.update()

    def __create_data_column(self, label: str, on_click):
        return ft.DataColumn(
            label=ft.Text(value=label.capitalize(), color='blue'),
            tooltip=f'Ordenar por {label.lower()}',
            on_sort=on_click,
        )

    def __create_data_cell(self, value: str, product_reference=None, column_reference=None):
        return ft.DataCell(ft.Text(value=value), on_tap=self.__handle_on_tap_cell, data={'product': product_reference, 'column': column_reference})

    def __create_data_row(self, product):
        return ft.DataRow(
            cells=[
                self.__create_data_cell(value=getattr(product, column.value[1]), product_reference=product, column_reference=column.value[0])
                for column in Column
            ]
        )

    def __update_table(self):
        self.rows = [self.__create_data_row(product) for product in self.__products]
    
    def __handle_on_sort_column(self, event):
        column_name = event.control.label.value.upper()
        attr_name = self.__column_to_attribute_map[column_name]
        self.__column_state_order[column_name] = not self.__column_state_order[column_name]
        self.__products.sort(
            key=lambda product: getattr(product, attr_name),
            reverse=self.__column_state_order[column_name]
        )
        self.__update_table()
        self.update()

    def __handle_on_tap_cell(self, event: ft.ControlEvent):
        cell: ft.DataCell = event.control
        if cell.data['column'] not in self.__non_editable_columns:
            self.__convert_to_text_field(event)
    
    def __convert_to_text_field(self, event: ft.ControlEvent):
        self.__selected_cell: ft.DataCell = event.control
        self.__update_cell_content(ft.TextField(label='Edit', autofocus=True, on_submit=self.__convert_to_text))

    def __convert_to_text(self, event: ft.ControlEvent):
        self.__selected_txt_field: ft.TextField = event.control
        self.__update_cell_content(ft.Text(value=self.__selected_txt_field.value))

    def __update_cell_content(self, new_content):
        self.__selected_cell.content = new_content
        self.__selected_cell.update()
