import flet as ft


class PageEvents:

    def clear_page(self, event: ft.ControlEvent):
        event.page.clean()
    
    def update_page(self, event: ft.ControlEvent):
        event.page.update()
    
    def open_drawer(self, event: ft.ControlEvent):
        event.page.drawer.open = True
        event.page.update()
    
    def close_drawer(self, event: ft.ControlEvent):
        event.page.drawer.open = False
        event.page.update()
    
    def change_appbar_title(self, title: str, icon: str, event: ft.ControlEvent):
        event.page.appbar.title = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(icon),
                ft.Text(title),
            ]
        )
    
    def add_to_page(self, content: ft.Control, event: ft.ControlEvent):
        event.page.add(content)
        