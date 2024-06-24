import flet as ft

from users.user             import User
from views.AppView          import AppView
from theme.theme_config     import LightTheme, DarkTheme


class LoginForm(ft.Card):
    
    HEIGHT       = 50
    ELEVATION    = 15
    WIDTH        = 300
    BORDER       = ft.InputBorder.NONE
    INPUT_FILTER = ft.InputFilter(regex_string=r'^[a-z0-9]*$') # Only lowercase letters and numbers
    STYLE        = ft.ButtonStyle(shape={'': ft.RoundedRectangleBorder(radius=8)})

    def __init__(self, on_login_click=None, on_close_click=None):
        super().__init__()
        self.txt_field_username = self._create_text_field('Usuario', 'person')
        self.txt_field_password = self._create_text_field('Contraseña', 'lock', password=True, can_reveal_password=True)
        btn_login = self._create_button('Iniciar sesión', on_login_click)
        btn_close = self._create_button('Cerrar', on_close_click)
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Lottie(
                        src='https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/A.json',
                        repeat=True,
                        # reverse=False,
                        animate=True,
                    ),
                    ft.Text('Inicio de sesión', size=24, weight=ft.FontWeight.BOLD, color=DarkTheme.primary_color),
                    ft.Text('Ingresa tus credenciales de acceso.', size=13,),
                    self.txt_field_username,
                    self.txt_field_password,
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

    @property
    def username(self) -> str | None:
        return self.txt_field_username.value
    
    @property
    def password(self) -> str | None:
        return self.txt_field_password.value

    def _create_text_field(self, label: str, icon: str, password: bool = False, can_reveal_password: bool = False) -> ft.TextField:
        return ft.TextField(
            label=label,
            icon=icon,
            width=self.WIDTH,
            height=self.HEIGHT,
            border=self.BORDER,
            input_filter=self.INPUT_FILTER,
            password=password,
            can_reveal_password=can_reveal_password,
        )
    
    def _create_button(self, label: str, on_click=None) -> ft.ElevatedButton:
        return ft.ElevatedButton(
            text=label,
            style=self.STYLE,
            width=self.WIDTH,
            height=self.HEIGHT,
            elevation=self.ELEVATION,
            on_click=on_click,
        )


class LoginView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = 'login/'

        page.window.width           = 340
        page.window.height          = 500
        page.window.frameless       = True
        page.theme                  = LightTheme
        page.theme_mode             = ft.ThemeMode.LIGHT
        page.vertical_alignment     = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment   = ft.CrossAxisAlignment.CENTER
        page.window.center()

        self.controls = [
            ft.Container(
                content=LoginForm(
                    on_login_click=self.handler_on_login_click,
                    on_close_click=self.handler_on_close_click,
                ),
                alignment=ft.alignment.center,
                expand=True,
                expand_loose=True,
            )
        ]
    
    def handler_on_login_click(self, event: ft.ControlEvent):
        pass

    def handler_on_close_click(self, event: ft.ControlEvent):
        page: ft.Page = event.page
        page.window.close()


    
    
    def create_snackbar_message(self, message: str):
        return ft.SnackBar(
            content=ft.Row([ft.Text(message, size=13, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
            width=300,
            elevation=15,
            bgcolor='red',
        )
    
    def show_not_found_user_msg(self, msg: str, event: ft.ControlEvent):
        snackbar = self.create_snackbar_message(msg)
        snackbar.open = True
        page: ft.Page = event.page
        page.overlay.append(snackbar)
        page.update()
    