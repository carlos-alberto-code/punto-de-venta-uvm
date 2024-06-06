import flet as ft
from interfaces.interfaces import ControllerInterface as Controller


class SearchBarHandler:

    def __init__(self, controller: Controller, table: ft.DataTable):
        self.controller = controller
        self.table = table

    def reset_product_table(self):
        pass
        # self.table.data = self.controller.get_all()
        # self.table.update()
        # print(self.table.data)
        

    def on_tap(self, event):
        searcher = event.control
        searcher.close_view('')
        self.reset_product_table()

    def on_change(self, event):
        searcher = event.control
        print('Se busca:', searcher.value)
