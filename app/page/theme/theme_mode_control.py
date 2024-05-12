import flet as ft


class ThemeModeButton(ft.IconButton):
    def __init__(self):
        super().__init__()
        # Colocar el ícono inicial en función de en qué modo se arrancó
        self.icon = ft.icons.DARK_MODE 
        self.on_click = self.change_mode    

    def change_mode(self, event: ft.ControlEvent):
        # Identificar el modo actual
        # Cambiar el modo
        # Cambiar el icono en función del modo
        event.page.theme_mode = ft.ThemeMode.LIGHT if event.page.theme == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        self.icon = ft.icons.LIGHT_MODE if self.icon == ft.icons.DARK_MODE else ft.icons.DARK_MODE
        event.page.update()
        self.update()
        