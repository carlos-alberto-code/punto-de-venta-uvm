import flet as ft

class AddProductButton(ft.PopupMenuItem):
    def __init__(self, on_click=None):
        super().__init__(
            text='Agregar nuevo producto',
            icon=ft.icons.ADD,
            on_click=on_click,
        )

        
class OptionsMenuButton(ft.PopupMenuButton):
    def __init__(self, *items: ft.PopupMenuItem):
        super().__init__(
            icon=ft.icons.MORE_VERT,
            items=[*items],
        )
