from typing import Optional
import flet as ft


ft.DataColumn(label=ft.TextButton('SKU'))
class Column(ft.DataColumn):
    def __init__(self, name: str, event: Optional[ft.ControlEvent] = None, is_numeric: bool = False):
        super().__init__(label=ft.Text(value=name), numeric=is_numeric)
        self.on_sort = event


ft.DataRow()
class Row(ft.DataRow):
    def __init__(self, *properties: str):
        super().__init__()
        self.cells = [ft.Text(value=prop) for prop in properties]


ft.DataTable()
class InventoryTable(ft.DataTable):
    def __init__(
            self,
            columns: list[ft.DataColumn] = [],
            rows: list[ft.DataRow] = [],
            
    ):
        super().__init__(columns=columns, rows=rows)
        self.show_checkbox_column = True
        self.on_select_all = lambda _: print('Select all')

    def func(self):
        pass
        



# Ambiente de depuración

def main(page: ft.Page):
    col1 = Column('SKU', print('Ordenando la tabla'), is_numeric=True)
    col2 = Column('UNIDAD')

    row1 = Row('744411', 'kilogramo')

    table = InventoryTable(columns=[col1, col2], rows=[row1])
    print(table.columns)
    print(table.rows)
    page.add(table)

ft.app(target=main)