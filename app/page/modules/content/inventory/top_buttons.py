import flet as ft


class AddNewButton(ft.FilledButton):
    def __init__(self):
        super().__init__(
            text='Nuevo producto',
            icon='add',
            on_click=lambda _: print('Nuevo producto'),
        )


class ShareButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__(
            icon=ft.icons.SHARE,
            menu_position=ft.PopupMenuPosition.UNDER,
        )
        self.items = [
           ft.PopupMenuItem(text='PDF', icon=ft.icons.PICTURE_AS_PDF_ROUNDED),
           ft.PopupMenuItem(text='CSV', icon=ft.icons.DATASET),
           ft.PopupMenuItem(text='BACKUP', icon=ft.icons.BACKUP)
        ]


class FilterButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__(
            icon=ft.icons.FILTER_LIST,
            menu_position=ft.PopupMenuPosition.UNDER,
        )
        self.items = [
            ft.PopupMenuItem(text='Categoria', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE),
            ft.PopupMenuItem(text='Marca', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE),
            ft.PopupMenuItem(text='Unidad', icon=ft.icons.ARROW_DROP_DOWN_CIRCLE)
        ]