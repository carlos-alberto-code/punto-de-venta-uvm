import flet as ft

from repository.controllers import SuplierController

from modules.suppliers_view.SupplierForm import SupplierForm
from modules.suppliers_view.SupplierTable import SupplierTable
from modules.suppliers_view.searchers import SupplierSearcher


supplier_controller = SuplierController() # Instancia del controlador de proveedores

supplier_form = SupplierForm() # Instancia del formulario de proveedores

def open_form(event: ft.ControlEvent): # Función (evento) para abrir el formulario
    page = event.page
    page.dialog = supplier_form
    page.dialog.open = True
    page.update()
    
add_product_option = ft.PopupMenuItem( # Opción para agregar un proveedor
    text='Agregar proveedor',
    icon=ft.icons.ADD,
    on_click=open_form,
)

# Código para otras opciones
# --------------------------

options_button = ft.PopupMenuButton( # Botón de opciones: Sólo tiene la opción de agregar un proveedor
    icon=ft.icons.MORE_VERT,
    items=[add_product_option],
)

# Supplier Table
supplier_table = SupplierTable(supplier_controller.get_all())

# Supplier Searcher
supplier_searcher = SupplierSearcher(supplier_controller, supplier_table) # Instancia del buscador de proveedores


class ContentStockSectionShape(ft.Column): # Capa de sección del inventario

    def __init__(self):
        super().__init__(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row( # Fila de controles: Buscador de productos, botón de opciones, contenedor
                    [   
                        supplier_searcher,
                        options_button,
                        ft.Container(width=45),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Column(
                    [
                        supplier_table,
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                )
            ]
        )