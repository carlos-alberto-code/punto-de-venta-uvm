import flet as ft


class PointOfSaleModule(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.View(
            route="point-of-sale",
            controls=[
                ft.Text("Point of Sale")
            ]
        )

