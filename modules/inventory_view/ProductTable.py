import flet as ft
from enum import Enum
from repository.controllers import ProductController


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
        self.__currently_edited_cell = None

        self.__product_controller = ProductController()
        
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
            label=ft.Text(value=label.capitalize(), color='#D9525E'),
            tooltip=f'Ordenar por {label.lower()}',
            on_sort=on_click,
        )

    def __create_data_cell(self, value: str, product_reference=None, column_reference=None):
        return ft.DataCell(ft.Text(value=value), on_tap=self.__handle_on_tap_cell, data={'product': product_reference, 'column': column_reference})

    def __create_data_row(self, product):
        return ft.DataRow(
            cells=[
                self.__create_data_cell(value=getattr(product, column.value[1]), product_reference=product, column_reference=column.value)
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
        # TODO: Existe un bug en donde la actualización de celda maneja una variable que cambia de tipo de datos, en algunas veces es un ft.TextField y en otras es un ft.Text, esto ocasiona que cuando detecta el ft.TextField detecte un valor vacío y no pueda convertir a float. Pero un manejo de excepciones normal no puede lidiar con una situación como esta.
        cell: ft.DataCell = event.control
        if cell.data['column'][0] not in self.__non_editable_columns and self.__currently_edited_cell is None: # type: ignore
            self.__currently_edited_cell = cell
            self.__convert_to_text_field(event)
    
    def __convert_to_text_field(self, event: ft.ControlEvent):
        self.__selected_cell: ft.DataCell = event.control
        self.__update_cell_content(ft.TextField(label='Edit', autofocus=True, on_submit=self.__convert_to_text))

    def __convert_to_text(self, event: ft.ControlEvent):
        self.__selected_txt_field: ft.TextField = event.control
        self.__update_cell_content(ft.Text(value=self.__selected_txt_field.value))
        self.__currently_edited_cell = None

    def __update_cell_content(self, new_content):
        self.__selected_cell.content = new_content
        self.__selected_cell.update()
        prod_id = self.__selected_cell.data['product'].id # type: ignore
        atrr = self.__selected_cell.data['column'][1] # type: ignore
        self.__product_controller.update(prod_id, **{atrr: float(new_content.value)})
        self.products = self.__product_controller.get_all()
        self.__show_snack_bar(self.page)

    def __show_snack_bar(self, page):
        snack_bar = ft.SnackBar(content=ft.Text(value='Producto actualizado correctamente'), bgcolor='blue')
        snack_bar.open = True
        page.overlay.append(snack_bar)
        page.update()
