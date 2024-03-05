import flet as ft


class SalesModule(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.View(
            route="sales",
            controls=[
                ft.Text("Sales")
            ]
        )

