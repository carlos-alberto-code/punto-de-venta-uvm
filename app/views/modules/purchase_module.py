import flet as ft


class PurchaseModule(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.View(
            route="purchase",
            controls=[
                ft.Text("Purchase")
            ]
        )

