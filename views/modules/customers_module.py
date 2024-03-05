import flet as ft


class CustomersModule(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
    
    def build(self):
        return ft.View(
            route="customers",
            controls=[
                ft.Text("Customers")
            ]
        )
