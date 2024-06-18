import flet as ft
from enum import Enum


class ColumnNames(Enum):
    """
    Represents the column names for the inventory table view.
    """
    NAME = 'NOMBRE'
    PHONE = 'TELEFONO'
    EMAIL = 'CORREO'
    ADDRESS = 'DIRECCION'

    def __iter__(self):
        yield from self.__dict__.values()


class SupplierAttributes(Enum):
    """
    Represents the attributes of a supplier.
    """
    NAME = 'name'
    PHONE = 'phone'
    EMAIL = 'email'
    ADDRESS = 'address'

    def __iter__(self):
        yield from self.__dict__.values()
    
    def __len__(self):
        return len(self.__dict__)


column_state_order = {
    column_name.value: True 
    for column_name in ColumnNames
}

column_to_attribute_map = {
    column_name.value: supplier_attribute.value
    for column_name, supplier_attribute 
    in zip(ColumnNames, SupplierAttributes)
}


class SupplierTable(ft.DataTable):

    def __init__(self, suppliers: list):
        super().__init__(
            columns=[
                self._create_data_column(
                    label=column_name.value,
                    on_click=self.sort_suppliers
                ) for column_name in ColumnNames
            ],
            border=ft.border.all(width=1, color=ft.colors.GREY_300),
            border_radius=15,
        )
        self._suppliers = suppliers
        self.update_table()
    
    @property
    def suppliers(self):
        return self._suppliers
    
    @suppliers.setter
    def suppliers(self, suppliers: list):
        self._suppliers = suppliers
        self.update_table()
        self.update()
    
    @staticmethod
    def _create_data_cell(value: str):
        return ft.DataCell(ft.Text(value=value))
    
    def _create_data_row(self, supplier):
        return ft.DataRow(
            cells=[
                self._create_data_cell(value=getattr(supplier, attr.value))
                for attr in SupplierAttributes
            ]
        )
    
    @staticmethod
    def _create_data_column(label: str, on_click):
        return ft.DataColumn(
            label=ft.Text(value=label.capitalize(), color='blue'),
            tooltip=f'Ordenar por {label.lower()}',
            on_sort=on_click
        )
    
    def update_table(self):
        self.rows = [self._create_data_row(supplier) for supplier in self._suppliers]
    
    def sort_suppliers(self, event):
        column_name = event.control.label.value.upper()
        attr_name = column_to_attribute_map[column_name]
        column_state_order[column_name] = not column_state_order[column_name]
        self._suppliers.sort(
            key=lambda supplier: getattr(supplier, attr_name),
            reverse=column_state_order[column_name]
        )
        self.update_table()
        self.update()