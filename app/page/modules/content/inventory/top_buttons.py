import flet as ft


class AddNewButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__(
            text='Nuevo',
            icon='add',
        )


class ShareButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__(
            icon=ft.icons.SHARE_OUTLINED,
            menu_position=ft.PopupMenuPosition.UNDER,
        )
        self.items = [
           ft.PopupMenuItem(text='PDF', icon=ft.icons.PICTURE_AS_PDF_ROUNDED),
           ft.PopupMenuItem(text='CSV', icon=ft.icons.DATASET),
           ft.PopupMenuItem(text='BACKUP', icon=ft.icons.BACKUP)
        ]