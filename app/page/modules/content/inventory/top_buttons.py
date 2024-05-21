import flet as ft

from controllers.products_controller import ProductController
from flet import PopupMenuItem


ft.PopupMenuItem()
class AddNewButton(ft.PopupMenuItem):
    def __init__(self, product_controller: ProductController):
        super().__init__(
            text='Nuevo producto',
            icon=ft.icons.ADD,
            on_click=self.open_form,
        )
    
    def open_form(self, event):

        def clear_form(event):
            form.clean()
            form.update()
            event.page.update()
        
        def save_product(event):
            pass

        form = ft.AlertDialog(
            title=ft.Text('Nuevo producto'),
            icon=ft.Icon(str(ft.icons.BACKUP_TABLE_OUTLINED)),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextField(label='Unidad'),
                        ft.TextField(label='Categoria'),
                        ft.TextField(label='Marca'),
                        ft.TextField(label='Cantidad'),
                        ft.TextField(label='Precio de compra'),
                        ft.TextField(label='Precio de venta'),
                        ft.TextField(label='Existenicas mínimas'),
                    ],
                    # scroll=ft.ScrollMode.AUTO,
                )
            ),
            actions=[
                ft.ElevatedButton(text='Limpiar', on_click=clear_form),
                ft.ElevatedButton(text='Guardar', on_click=save_product),
            ],
            scrollable=True,
        )
        form.open = True
        event.page.dialog = form
        event.page.update()


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
