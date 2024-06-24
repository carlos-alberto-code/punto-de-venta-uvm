import flet as ft


class LoginForm(ft.Card):
    
    HEIGHT       = 50
    ELEVATION    = 15
    WIDTH        = 300
    BORDER       = ft.InputBorder.NONE
    INPUT_FILTER = ft.InputFilter(regex_string=r'^[a-z0-9]*$') # Only lowercase letters and numbers
    STYLE        = ft.ButtonStyle(shape={'': ft.RoundedRectangleBorder(radius=8)})

    def __init__(self, on_login_click=None, on_close_click=None, on_press_enter=None):
        super().__init__()
        self.txt_field_username = self._create_text_field('Usuario', 'person', on_press_enter=on_press_enter)
        self.txt_field_password = self._create_text_field('Contraseña', 'lock', password=True, can_reveal_password=True, on_press_enter=on_press_enter)
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
                    ft.Text('Inicio de sesión', size=24, weight=ft.FontWeight.BOLD),
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

    def _create_text_field(self, label: str, icon: str, password: bool = False, can_reveal_password: bool = False, on_press_enter=None) -> ft.TextField:
        return ft.TextField(
            label=label,
            icon=icon,
            width=self.WIDTH,
            height=self.HEIGHT,
            border=self.BORDER,
            input_filter=self.INPUT_FILTER,
            password=password,
            can_reveal_password=can_reveal_password,
            on_submit=on_press_enter,
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