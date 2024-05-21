import flet as ft

from controllers.products_controller import ProductController
from page.modules.content.inventory.ProductForm import ProductForm
from page.components.search_bar_filter.properties_controller import UnitFilter, CategoryFilter, BrandFilter

ft.PopupMenuItem()
class AddNewButton(ft.PopupMenuItem):
    def __init__(self, product_controller: ProductController):
        super().__init__(
            text='Nuevo producto',
            icon=ft.icons.ADD,
        )
        self.product_form = ProductForm(
            Categoria=CategoryFilter(),
            Marca=BrandFilter(),
            Unidad=UnitFilter(),
        )
        self.on_click = self.open_form
    
    def open_form(self, event):
        self.product_form.open = True
        event.page.add(self.product_form)


class ShareButton(ft.PopupMenuItem):
    def __init__(self):
        super().__init__()
        self.text = 'Exportar'
        self.icon = ft.icons.FILE_DOWNLOAD
        # self.content = ft.PopupMenuButton(
        #     # tooltip='Exportar',
        #     # content=ft.Row(
        #     #     [
        #     #         ft.Icon(str(ft.icons.FILE_DOWNLOAD)), ft.Text('Exportar')
        #     #     ]
        #     # ),
        #     menu_position=ft.PopupMenuPosition.UNDER,
        #     items=[
        #         ft.PopupMenuItem(text='CSV', icon=ft.icons.DATASET),
        #         ft.PopupMenuItem(text='PDF', icon=ft.icons.PICTURE_AS_PDF),
        #         ft.PopupMenuItem(text='BACKUP', icon=ft.icons.BACKUP)
        #     ]
        # )
        self.on_click = self.open_drawer_r

    def open_drawer_r(self, event):
        filer = ft.FilePicker()
        event.page.add(filer)
        filer.pick_files()

ft.PopupMenuButton()
class MenuOptionsButton(ft.PopupMenuButton):
    def __init__(self, product_controller: ProductController):
        super().__init__(
            icon=ft.icons.MORE_VERT,
            tooltip='Opciones',
            menu_position=ft.PopupMenuPosition.UNDER,
            items=[
                AddNewButton(product_controller),  # Add the product_controller argument here
                ShareButton(),
            ]
        )
