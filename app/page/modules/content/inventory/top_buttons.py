import flet as ft

from controllers.products_controller import ProductController
from page.modules.content.inventory.ProductForm import ProductForm
from page.components.search_bar_filter.properties_controller import UnitFilter, CategoryFilter, BrandFilter

# Exportar
# Agregar nuevo producto
# Filtros
# Busqueda general

class AddNewButton(ft.IconButton):
    def __init__(self, product_controller: ProductController):
        super().__init__(
            icon=ft.icons.ADD,
            tooltip='Registrar nuevo producto'
        )
        self.product_form = ProductForm()
        self.on_click = self.open_form
    
    def open_form(self, event):
        self.product_form.open = True
        event.page.add(self.product_form)

ft.PopupMenuButton()
class FilterButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__(
            icon=ft.icons.FILTER_LIST,
            items=[
                ft.PopupMenuItem(text='Unidad', icon=ft.icons.ARROW_RIGHT),
                ft.PopupMenuItem(text='Categoria', icon=ft.icons.ARROW_RIGHT),
                ft.PopupMenuItem(text='Marca', icon=ft.icons.ARROW_RIGHT),
            ]
        )


class ShareButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__()
        self.icon = ft.icons.FILE_DOWNLOAD_OUTLINED
        self.items=[
                ft.PopupMenuItem(text='CSV', icon=ft.icons.DATASET),
                ft.PopupMenuItem(text='PDF', icon=ft.icons.PICTURE_AS_PDF),
                ft.PopupMenuItem(text='BACKUP', icon=ft.icons.BACKUP)
            ]


