from typing import Optional
import flet as ft

from .components.counter import Counter, IntCounter


def create_username(fullname: str, age: int) -> str:
    name = fullname.split(' ')[0]
    return f'{name}{age}'



class LoginPage(ft.UserControl):

    def __init__(self, page: ft.Page):
        self.page = page
        page.vertical_alignment   = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window_width  = 450
        page.window_height = 400
        page.window_center()
        self.title = ft.Text(
            value='Sign in',
            size=25,
        )
        self.fullname = ft.TextField(
            label='Tu nombre completo',
        )
        self.age_text = ft.Text(
            value='Edad',
        )
        # Casilla de verificación que indique si es o no propietario
        self.is_owner = ft.Checkbox(
            label='Soy propietario',
        )
        self.button_create_user = ft.FilledButton(
            text='Crear una cuenta',
        )

    def build(self):
        counter = Counter(IntCounter()).build()
        # Agrega los controles a la página
        container = ft.Container(
            content=ft.Column(
                controls=[
                    self.title,
                    self.fullname,
                    self.age_text,
                    counter,
                    self.is_owner,
                    self.button_create_user
                ]
            )
        )
        # Ahora que los controles se han agregado a la página, puedes actualizarlos
        return container
