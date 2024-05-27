import flet as ft

from page.interfaces.ControllerInterface import IController


class Form:
    pass


ft.AlertDialog()
class AlertForm(ft.AlertDialog):

    def __init__(self, title: str):
        super().__init__(
            title=ft.Text(title),
            actions=[
                ft.ElevatedButton("Cancelar"),
                ft.ElevatedButton('Limpiar'),
                ft.ElevatedButton("Guardar"),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.controller = Repository()
        self.controller.create()
    