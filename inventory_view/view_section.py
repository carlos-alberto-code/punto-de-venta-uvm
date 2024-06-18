import flet as ft

from controllers.controllers import ProductController

from inventory_view.ProductForm import ProductForm
from inventory_view.ProductTable import ProductTable
from components.searchers import ProductSearcher


prod_controller = ProductController() # Instancia del controlador de productos

product_form = ProductForm() # Instancia del formulario de productos

def open_form(event: ft.ControlEvent): # Función (evento) para abrir el formulario
    page = event.page
    page.dialog = product_form
    page.dialog.open = True
    page.update()
    
add_product_option = ft.PopupMenuItem( # Opción para agregar un producto
    text='Agregar producto',
    icon=ft.icons.ADD,
    on_click=open_form,
)

# Código para otras opciones
# --------------------------

options_button = ft.PopupMenuButton( # Botón de opciones: Sólo tiene la opción de agregar un producto
    icon=ft.icons.MORE_VERT,
    items=[add_product_option],
)

# Product Table
product_table = ProductTable(prod_controller.get_all())

# Product Searcher
product_searcher = ProductSearcher(prod_controller, product_table) # Instancia del buscador de productos


class ContentStockSectionShape(ft.Column): # Capa de sección del inventario

    def __init__(self):
        super().__init__(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row( # Fila de controles: Buscador de productos, botón de opciones, contenedor
                    [   
                        product_searcher,
                        options_button,
                        ft.Container(width=45),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Column(
                    [
                        product_table,
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                )
            ]
        )