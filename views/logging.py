import flet as ft

from .color_palette import ColorPalette


class IconTextField(ft.UserControl):

    def __init__(self, label: str, icon: ft.Icon, color_palette: ColorPalette) -> None:
        super().__init__()
        self.text_field = ft.TextField(
            height=40,
            text_size=13,
            label_style=ft.TextStyle(size=13, color=color_palette.TEXT),
            expand=True,
            text_vertical_align=ft.VerticalAlignment.CENTER,
            label=label,
            border_radius=15,
            border_color=color_palette.SURFACE
        )
        self.icon = icon
        self.icon.color = color_palette.SURFACE

    def build(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.icon,
                self.text_field
            ]
        )
        


class LoggingView(ft.UserControl):

    def __init__(self, page: ft.Page, color_palette: ColorPalette) -> None:
        super().__init__()
        self.color_palette = color_palette
        # Configuración de la ventana de windows
        self._configure_window(page)
        self._create_title()
        self._create_text_fields()

    def _configure_window(self, page: ft.Page):
        page.bgcolor = self.color_palette.BACKGROUND
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.LIGHT
        # page.window_maximizable = False
        # page.window_frameless = True
        # page.window_height = 400
        # page.window_width = 350
        # page.window_center()
        page.padding = 10

    def _create_title(self):
        self.title = ft.Text('Inicio de sesión', size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color=self.color_palette.SURFACE)

    def _create_text_fields(self):
        self.username = IconTextField(label='Nombre de usuario', icon=ft.Icon(name=ft.icons.PEOPLE), color_palette=self.color_palette)
        self.password = IconTextField(label='Contraseña', icon=ft.Icon(name=ft.icons.LOCK), color_palette=self.color_palette)
        self.username.text_field.autofocus = True
        self.password.text_field.password = True
        self.password.text_field.can_reveal_password = True

    def build(self):
        return ft.Container(
            # bgcolor=self.color_palette.SECONDARY,
            adaptive=True,
            padding=30,
            border_radius=15,
            border=ft.border.all(color=self.color_palette.SURFACE),
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.title], alignment=ft.MainAxisAlignment.CENTER), # Aqui se modifica la posición
                    ft.Divider(color=self.color_palette.SURFACE),
                    self.username,
                    ft.Divider(opacity=0, height=1),
                    self.password,
                    ft.Divider(opacity=0, height=1),
                    ft.Row(
                        controls=[
                            ft.FilledButton(text='Entrar', style=ft.ButtonStyle(bgcolor=self.color_palette.SURFACE, color=ColorPalette.BACKGROUND), expand=True,)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    # ft.Divider(opacity=0, height=0),
                    ft.Row(
                        controls=[
                            ft.TextButton(text='¿Olvidaste tu contraseña?')
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START
                    ),
                ]
            )
        )



# class Logging()