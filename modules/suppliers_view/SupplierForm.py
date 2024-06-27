import flet as ft

from components.counters import IntCounter
from components.searchers import SimpleModelSearcher
from repository.controllers import UnitController, CategoryController, BrandController, ProductController, SuplierController


class ContentShape(ft.Column):

    def __init__(
            self,
            name_field: ft.Control,
            phone_field: ft.Control,
            email_field: ft.Control,
            address_field: ft.Control


    ):
        super().__init__(
            controls=[
                ft.Row([ft.Text(value='Nombre'), name_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([ft.Text(value='Telefono'), phone_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([ft.Text(value='Correo'), email_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([ft.Text(value='Direccion'), address_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ]
        )


class SupplierForm(ft.AlertDialog):

    def __init__(self):
        super().__init__(
            title=ft.Row([ft.Text(value='Nuevo proveedor')], alignment=ft.MainAxisAlignment.CENTER),
            icon=ft.Icon(name=ft.icons.PEOPLE),
            scrollable=True,
            actions=[
                ft.ElevatedButton(text='Cancelar', on_click=self._cancel_form),
                ft.ElevatedButton(text='Guardar', on_click=self._save_data_form),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        #self.name_searcher = SimpleModelSearcher(SuplierController())
        #self.phone_searcher = SimpleModelSearcher(SuplierController())
        #self.email_searcher = SimpleModelSearcher(SuplierController())
        #self.address_searcher = SimpleModelSearcher(SuplierController())
        self.name_searcher = ft.TextField(label='nombre', width=150)
        self.phone_searcher = ft.TextField(label='telefono', width=150)
        self.email_searcher = ft.TextField(label='correo', width=150)
        self.address_searcher = ft.TextField(label='direccion', width=150)

        #Configuracion de los searchers
        #self.name_searcher.bar_hint_text = 'Selecciona un nombre'
        #self.phone_searcher.bar_hint_text = 'Selecciona un telefono'
        #self.email_searcher.bar_hint_text = 'Selecciona un correo'
        #self.address_searcher.bar_hint_text = 'Selecciona una direccion'
        #content
        self.content = ContentShape(
            name_field=self.name_searcher,
            phone_field=self.phone_searcher,
            email_field=self.email_searcher,
            address_field=self.address_searcher
        )
        """self.unit_searcher = SimpleModelSearcher(UnitController())
        self.category_searcher = SimpleModelSearcher(CategoryController())
        self.brand_searcher = SimpleModelSearcher(BrandController())
        # Configuración de los searchers
        self.unit_searcher.bar_hint_text = 'Selecciona una unidad'
        self.category_searcher.bar_hint_text = 'Selecciona una categoría'
        self.brand_searcher.bar_hint_text = 'Selecciona una marca'
        # Contadores
        self.quantity_counter = Counter()
        self.cost_counter = Counter()
        self.sell_price_counter = Counter()
        self.reorder_level_counter = Counter()
        self.content = ContentShape(
            unit_field=self.unit_searcher,
            category_field=self.category_searcher,
            brand_field=self.brand_searcher,
            quantity_field=self.quantity_counter,
            cost_field=self.cost_counter,
            sell_price_field=self.sell_price_counter,
            reorder_level_field=self.reorder_level_counter,
        )"""
    
    # Action Events (Handlers)

    def _cancel_form(self, event: ft.ControlEvent):
        self._reset_form()
        self.open = False
        event.page.update()
    
    def _reset_form(self):
        self.name_searcher.value = ''
        self.phone_searcher.value = ''
        self.email_searcher.value = ''
        self.address_searcher.value = ''
        """self.unit_searcher.value = ''
        self.category_searcher.value = ''
        self.brand_searcher.value = ''
        self.quantity_counter.value = 1
        self.cost_counter.value = 1
        self.sell_price_counter.value = 1
        self.reorder_level_counter.value = 1"""
    
    
    def _save_data_form(self, event: ft.ControlEvent):
        supplier_controller = SuplierController()
        if self.name_searcher.value\
        and self.phone_searcher.value\
        and self.email_searcher.value\
        and self.address_searcher.value:    
            self.data = {
                'name': self.name_searcher.value,
                'phone': self.phone_searcher.value,
                'email': self.email_searcher.value,
                'address': self.address_searcher.value,
            }
            supplier_controller.insert(
                name=self.data['name'],
                phone=self.data['phone'],
                email=self.data['email'],
                address=self.data['address'],
            )
            self._close_form(event)
            self._reset_form()
            self._open_ok_snack_bar(event)
        else:
            self.show_error_snack_bar(event)
    
    def _open_ok_snack_bar(self, event: ft.ControlEvent):
        event.page.snack_bar = ft.SnackBar(
            bgcolor=ft.colors.BLUE,
            content=ft.Text(value='Proveedor guardado con éxito'),
        )
        event.page.snack_bar.open = True
        event.page.update()
    
    def _close_form(self, event: ft.ControlEvent):
        event.page.dialog.open = False
        event.page.update()
    
    def show_error_snack_bar(self, event: ft.ControlEvent):
        event.page.snack_bar = ft.SnackBar(
            bgcolor=ft.colors.RED,
            content=ft.Text(value='Error al guardar el proveedor: Los campos no pueden estar vacíos'),
        )
        event.page.snack_bar.open = True
        event.page.update()