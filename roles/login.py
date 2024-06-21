import flet as ft
from theme.theme_config import LightTheme, DarkTheme


class Login(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        txt_field_username = ft.TextField(
            label='Nombre de usuario',
            icon='person',
            width=300,
            height=50,
            autofocus=True,
            border=ft.InputBorder.UNDERLINE,
            input_filter=ft.InputFilter(
                # Sólo permitir letras minusculas y números, pero no caracteres especiales
                regex_string=r'^[a-z0-9]*$',
            )
        )

        txt_field_password = ft.TextField(
            label='Contraseña',
            icon='lock',
            width=300,
            height=50,
            password=True,
            can_reveal_password=True,
            border=ft.InputBorder.UNDERLINE,
            input_filter=ft.InputFilter(
                # Sólo permitir letras minusculas y números, pero no caracteres especiales
                regex_string=r'^[a-z0-9]*$',
            )
        )

        btn_login = ft.ElevatedButton(
                content=ft.Text('Iniciar sesión', size=13, weight=ft.FontWeight.BOLD),
                style=ft.ButtonStyle(
                    shape={'': ft.RoundedRectangleBorder(radius=8)},
                ),
                width=300,
                height=42,
                elevation=15,
        )
        
        btn_close = ft.ElevatedButton(
            content=ft.Text('Salir', size=13, weight=ft.FontWeight.BOLD),
                style=ft.ButtonStyle(
                    shape={'': ft.RoundedRectangleBorder(radius=8)},
            ),
            width=300,
            height=42,
            elevation=15,
            on_click=lambda e: page.window.close(),
        )

        content = ft.Card(
            width=400,
            expand=True,
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Lottie(
                            src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
                            repeat=True,
                            # reverse=False,
                            animate=True,
                        ),
                        ft.Text('Inicio de sesión', size=24, weight=ft.FontWeight.BOLD),
                        ft.Text('Ingresa tus credenciales de acceso.', size=13,),
                        txt_field_username,
                        txt_field_password,
                        btn_login,
                        btn_close,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                ),
                padding=10,
                border_radius=15,
            )
        )
        page.window.width = 400
        page.window.height = 580
        page.theme_mode = ft.ThemeMode.LIGHT
        page.theme = LightTheme
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window.frameless = True
        page.add(content)
        page.window.center()
