from typing import List
import flet as ft


# Icons
_close_icon        = ft.icons.CLOSE
_dark_mode_icon    = ft.icons.DARK_MODE
_light_mode_icon   = ft.icons.LIGHT_MODE
_notification_icon = ft.icons.NOTIFICATIONS


class AppbarActions:

    def __init__(self, theme_mode: ft.ThemeMode = ft.ThemeMode.LIGHT) -> None:
        self.theme_mode     = theme_mode
        self.theme_button   = ft.IconButton(icon=self._get_theme_icon(), on_click=self._toggle_theme, tooltip='Cambiar el tema')
        self.close_button   = ft.IconButton(icon=_close_icon, on_click=self._close_app, tooltip='Cerrar la app')
        self.notification   = ft.IconButton(icon=_notification_icon, tooltip='Notificaciones')
    
    @property
    def controls(self) -> List[ft.Control]:
        return [self.theme_button, self.notification,self.close_button]

    def _get_theme_icon(self) -> str:
        return _light_mode_icon if self.theme_mode == ft.ThemeMode.DARK else _dark_mode_icon
    
    def _toggle_theme(self, event: ft.ControlEvent):
        self.theme_mode = ft.ThemeMode.DARK if self.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self.theme_button.icon = self._get_theme_icon()
        event.page.theme_mode = self.theme_mode
        event.page.update()
    
    def _close_app(self, event: ft.ControlEvent):
        event.page.window_close()
        