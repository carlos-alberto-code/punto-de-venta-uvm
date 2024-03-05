import flet as ft


class ReportsModule(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.View(
            route="reports",
            controls=[
                ft.Text("Reports")
            ]
        )

