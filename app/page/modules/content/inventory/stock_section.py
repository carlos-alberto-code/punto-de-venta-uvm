import flet as ft

from page.modules.content.inventory.ProductTable    import ProductTable
from page.modules.content.inventory.searchers       import ProductSearcher
from controllers.controllers                        import ProductController
from page.modules.content.inventory.OptionButtons   import OptionsMenuButton, AddProductButton

# Importaciones del Formulario de Producto
from page.modules.content.inventory.form.ProductForm     import ProductForm
from page.modules.content.inventory.form.FormEventHandler import FormEventHandler
from page.modules.content.inventory.form.form_actions import SaveButton, CancelButton, CleanButton


class StockSection(ft.Column):
    # Responsable de formar la estructura y el contexto de la sección de inventario
    def __init__(self):
        super().__init__(
            expand=True,
            # scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        self.product_controller = ProductController()

        # Definiendo el formulario de producto
        self.form = ProductForm()
        self.handler = FormEventHandler(
            controller=self.product_controller,
            form=self.form,
        )
        self.form.actions = [
            CancelButton(on_click=self.handler.cancel),
            CleanButton(on_click=self.handler.clean),
            SaveButton(on_click=self.handler.save),
        ]
        

        # Delcaración de los botones opcionales
        self.add_product_button = AddProductButton(on_click=self.handler_on_click_add_product)
        self.options_menu_button = OptionsMenuButton(self.add_product_button)

        # Declaración de los componentes de la sección de inventario
        self.product_searcher = ProductSearcher(on_change=self.handle_on_change_event, on_tap=self.handle_on_tap_event)


        products = self.product_controller.get_all()
        self.product_table = ProductTable(products)
        self.controls = [
            ft.Row( # SearchBarFilter, MenuOptionsButton, Container
                [   
                    
                    # Searcher('Productos', BrandFilter()),
                    self.product_searcher,
                    self.options_menu_button,
                    ft.Container(width=45)
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            ft.Column(
                [
                    self.product_table,
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )
        ]
    
    # Maneja el evento de cambio en el buscador
    def handle_on_change_event(self, event: ft.ControlEvent):
        control = event.control
        search_term = control.value
        results = self.product_controller.search(search_term)
        self.product_table.products = results
        
    # Maneja el evento de toque en el buscador
    def handle_on_tap_event(self, event: ft.ControlEvent):
        control = event.control
        search_term = control.value
        control.close_view()
        self.product_table.products = self.product_controller.get_all()

    # Evento para abrir el formulario de agregar producto
    def handler_on_click_add_product(self, event: ft.ControlEvent):
        event.page.dialog = self.form
        event.page.dialog.open = True
        event.page.update()
