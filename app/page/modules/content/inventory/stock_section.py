import flet as ft

from page.modules.content.inventory.ProductTable    import ProductTable
from page.modules.content.inventory.searchers       import ProductSearcher
from page.modules.content.inventory.top_buttons     import OptionsMenuButton
from controllers.controllers                        import ProductController


class StockSection(ft.Column):
    # Responsable de formar la estructura y el contexto de la sección de inventario
    def __init__(self):
        super().__init__(
            expand=True,
            # scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.product_controller = ProductController()
        products = self.product_controller.get_all()
        self.product_table = ProductTable(products)
        self.product_searcher = ProductSearcher(on_change=self.handle_on_change_event, on_tap=self.handle_on_tap_event)
        self.controls = [
            ft.Row( # SearchBarFilter, MenuOptionsButton, Container
                [   
                    
                    # Searcher('Productos', BrandFilter()),
                    self.product_searcher,
                    OptionsMenuButton(),
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
    
    def handle_on_change_event(self, event: ft.ControlEvent):
        control = event.control
        search_term = control.value
        results = self.product_controller.search(search_term)
        self.product_table.products = results
        
    def handle_on_tap_event(self, event: ft.ControlEvent):
        control = event.control
        search_term = control.value
        control.close_view()
        self.product_table.products = self.product_controller.get_all()
        