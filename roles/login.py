import flet as ft

from business_classes.user  import User
from roles.app_view         import AppView
from theme.theme_config     import LightTheme
from roles.authenticator    import Autenticator


class Login(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = 'login/'
        self.__view = page
        self.txt_field_username = ft.TextField(
            label='Nombre de usuario',
            icon='person',
            width=300,
            height=50,
            border=ft.InputBorder.NONE,
            input_filter=ft.InputFilter(
                # Sólo permitir letras minusculas y números, pero no caracteres especiales
                regex_string=r'^[a-z0-9]*$',
            )
        )

        self.txt_field_password = ft.TextField(
            label='Contraseña',
            icon='lock',
            width=300,
            height=50,
            password=True,
            can_reveal_password=True,
            border=ft.InputBorder.NONE,
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
                on_click=self.handle_on_login_click,
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
        )
        self._set_login_page_config(page, content)

    def _set_login_page_config(self, page: ft.Page, content):
        page.window.width = 400
        page.window.height = 580
        page.theme_mode = ft.ThemeMode.LIGHT
        page.theme = LightTheme
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window.frameless = True
        page.add(content)
        page.window.center()

    def _get_txt_fields_values(self):
        return {
            'username': str(self.txt_field_username.value),
            'password': str(self.txt_field_password.value),
        }
    
    def create_snackbar(self, message: str):
        return ft.SnackBar(
            content=ft.Row([ft.Text(message, size=13, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
            width=300,
            elevation=15,
            bgcolor='red',
        )
    
    def show_not_found_user_msg(self, msg: str, event: ft.ControlEvent):
        snackbar = self.create_snackbar(msg)
        snackbar.open = True
        page: ft.Page = event.page
        page.overlay.append(snackbar)
        page.update()
    
    def handle_on_login_click(self, event: ft.ControlEvent):
        user = self._get_txt_fields_values()
        authenticator = Autenticator(username=user['username'], password=user['password'])
        result = authenticator.authenticate()
        if isinstance(result, User):
            self.__view.views.clear()
            app = AppView(self.__view, user=result)
            self.__view.views.append(app)
            self.__view.go(app.route)
            self.__view.update()
            print(self.__view.route)
            
        else:
            self.show_not_found_user_msg(msg=str(result), event=event)
