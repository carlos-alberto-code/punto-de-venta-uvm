import flet as ft


class InventoryModule(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.View(
            route="inventory",
            controls=[
                ft.Text("Inventory")
            ]
        )

