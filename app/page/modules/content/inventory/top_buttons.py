import flet as ft

from page.components.Searcher import Searcher
from controllers.controllers import ProductController
from page.modules.content.inventory.ProductForm import ProductForm
from page.components.search_bar_filter.properties_controller import UnitFilter, CategoryFilter, BrandFilter


def open_searcher(event):
    f = ft.AlertDialog(
        title=ft.Text('Buscar producto'),
        content=Searcher('Productos', BrandFilter())
    )
    f.open = True
    event.page.add(f)


class SearchIconButton(ft.IconButton):
    def __init__(self):
        super().__init__()
        self.icon = ft.icons.SEARCH
        self.tooltip = 'Buscar producto'
        self.on_click = open_searcher



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


class ExportButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__()
        self.icon = ft.icons.FILE_DOWNLOAD_OUTLINED
        self.items=[
                ft.PopupMenuItem(text='CSV', icon=ft.icons.DATASET),
                ft.PopupMenuItem(text='PDF', icon=ft.icons.PICTURE_AS_PDF),
                ft.PopupMenuItem(text='BACKUP', icon=ft.icons.BACKUP)
            ]


class OptionsMenuButton(ft.PopupMenuButton):
    
    def __init__(self):
        super().__init__()
        self.icon = ft.icons.MORE_VERT
        self.items = [
            ft.PopupMenuItem(text='Filtar', icon=ft.icons.FILTER_LIST),
            ft.PopupMenuItem(text='Agregar nuevo producto', icon=ft.icons.ADD),
            ft.PopupMenuItem(text='Exportar', icon=ft.icons.FILE_DOWNLOAD_OUTLINED),
        ]
