import flet as ft

from components.counters import Counter
from components.searchers import SimpleModelSearcher
from controllers.controllers import UnitController, CategoryController, BrandController, ProductController


class ContentShape(ft.Column):

    def __init__(
            self,
            unit_field: ft.Control,
            category_field: ft.Control,
            brand_field: ft.Control,
            quantity_field: ft.Control,
            cost_field: ft.Control,
            sell_price_field: ft.Control,
            reorder_level_field: ft.Control,
    ):
        super().__init__(
            controls=[
                unit_field,
                category_field,
                brand_field,
                ft.Row([ft.Text(value='Cantidad'), quantity_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([ft.Text(value='Costo'), cost_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([ft.Text(value='Precio de venta'), sell_price_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Row([ft.Text(value='Nivel de reorden'), reorder_level_field], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ]
        )


class ProductForm(ft.AlertDialog):

    def __init__(self):
        super().__init__(
            title=ft.Row([ft.Text(value='Nuevo producto')], alignment=ft.MainAxisAlignment.CENTER),
            icon=ft.Icon(name=ft.icons.INVENTORY),
            scrollable=True,
            actions=[
                ft.ElevatedButton(text='Cancelar', on_click=self._cancel_form),
                ft.ElevatedButton(text='Guardar', on_click=self._save_data_form),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.unit_searcher = SimpleModelSearcher(UnitController())
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
        )
    
    # Action Events (Handlers)

    def _cancel_form(self, event: ft.ControlEvent):
        self._reset_form()
        self.open = False
        event.page.update()
    
    def _reset_form(self):
        self.unit_searcher.value = ''
        self.category_searcher.value = ''
        self.brand_searcher.value = ''
        self.quantity_counter.value = 1
        self.cost_counter.value = 1
        self.sell_price_counter.value = 1
        self.reorder_level_counter.value = 1
    
    
    def _save_data_form(self, event: ft.ControlEvent):
        prod_controller = ProductController()
        if self.unit_searcher.data\
        and self.category_searcher.data\
        and self.brand_searcher.data\
        and self.quantity_counter.value\
        and self.cost_counter.value\
        and self.sell_price_counter.value\
        and self.reorder_level_counter.value:    
            self.data = {
                'unit': self.unit_searcher.data,
                'category': self.category_searcher.data,
                'brand': self.brand_searcher.data,
                'quantity': self.quantity_counter.value,
                'cost_price': self.cost_counter.value,
                'selling_price': self.sell_price_counter.value,
                'reorder_level': self.reorder_level_counter.value,
            }
            prod_controller.insert(
                unit_id=self.data['unit']['id'],
                category_id=self.data['category']['id'],
                brand_id=self.data['brand']['id'],
                quantity=self.data['quantity'],
                cost_price=self.data['cost_price'],
                selling_price=self.data['selling_price'],
                reorder_level=self.data['reorder_level'],
            )
            self._close_form(event)
            self._reset_form()
            self._open_ok_snack_bar(event)
        else:
            self.show_error_snack_bar(event)
    
    def _open_ok_snack_bar(self, event: ft.ControlEvent):
        event.page.snack_bar = ft.SnackBar(
            bgcolor=ft.colors.BLUE,
            content=ft.Text(value='Producto guardado con éxito'),
        )
        event.page.snack_bar.open = True
        event.page.update()
    
    def _close_form(self, event: ft.ControlEvent):
        event.page.dialog.open = False
        event.page.update()
    
    def show_error_snack_bar(self, event: ft.ControlEvent):
        event.page.snack_bar = ft.SnackBar(
            bgcolor=ft.colors.RED,
            content=ft.Text(value='Error al guardar el producto: Los campos no pueden estar vacíos'),
        )
        event.page.snack_bar.open = True
        event.page.update()