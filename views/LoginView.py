import flet as ft

from users.session      import Session
from views.AppView      import AppView
from users.LoginForm    import LoginForm


class LoginView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route: str = 'login/'

        page.window.width           = 340
        page.window.height          = 500
        page.window.frameless       = True
        page.vertical_alignment     = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment   = ft.CrossAxisAlignment.CENTER
        page.window.center()

        self.login_form = LoginForm(
            on_login_click=self._handler_on_login_click,
            on_close_click=self._handler_on_close_click,
            on_press_enter=self._handler_on_login_click,
        )

        self.controls = [
            ft.Container(
                content=self.login_form,
                alignment=ft.alignment.center,
                expand=True,
                expand_loose=True,
            )
        ]
    
    def _handler_on_login_click(self, event: ft.ControlEvent):
        self._validate_data_exist(event)
        # Comprobar que las credenciales sean correctas
        if self.login_form.username and self.login_form.password:
            session = Session(username=self.login_form.username, password=self.login_form.password)
            if not session.user_exists():
                self._show_snackbar_message(f'El usuario {self.login_form.username} no existe.', event)
            elif not session.password_is_correct():
                self._show_snackbar_message('La contraseña es incorrecta.', event)
            else:
                page: ft.Page = event.page
                page.views.append(AppView(page=page, user=session.data))
                page.go('app/')

    def _validate_data_exist(self, event):
        if self.login_form.username == '':
            self._show_snackbar_message('Debes ingresar un nombre de usuario', event)
        if self.login_form.password == '':
            self._show_snackbar_message('Debes ingresar una contraseña', event)
    
    def is_user_valid(self):
        return

    def _handler_on_close_click(self, event: ft.ControlEvent): # Ready
        page: ft.Page = event.page
        page.window.close()
    
    def _create_snackbar(self, message: str):
        return ft.SnackBar(
            content=ft.Row([ft.Text(message, size=13, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
            width=300,
            elevation=15,
            bgcolor='red',
        )
    
    def _show_snackbar_message(self, msg: str, event: ft.ControlEvent):
        snackbar: ft.SnackBar = self._create_snackbar(msg)
        snackbar.open = True
        page: ft.Page = event.page
        page.overlay.append(snackbar)
        page.update()
    