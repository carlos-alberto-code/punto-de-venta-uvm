import flet as ft


ft.PopupMenuItem()
class AddNewButton(ft.PopupMenuItem):
    def __init__(self):
        super().__init__(
            text='Nuevo producto',
            icon=ft.icons.ADD,
            on_click=lambda _: print('Nuevo producto'),
        )


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

ft.PopupMenuButton()
class MenuOptionsButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__(
            icon=ft.icons.MORE_VERT,
            tooltip='Opciones',
            menu_position=ft.PopupMenuPosition.UNDER,
            items=[
                AddNewButton(),
                ShareButton(),
            ]
        )
