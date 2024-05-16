import flet as ft


ft.Tabs()
class ProductViews(ft.Tabs):
    
    def __init__(self, *views: ft.Tab):
        super().__init__(tabs=list(views))