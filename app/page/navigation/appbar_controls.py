from typing import List
import flet as ft


# Icons
_light_mode  = ft.icons.LIGHT_MODE
_dark_mode   = ft.icons.DARK_MODE
_close       = ft.icons.CLOSE
_chat        = ft.icons.STACKED_BAR_CHART_OUTLINED


class AppbarActions:

    def __init__(self, theme_mode: ft.ThemeMode = ft.ThemeMode.LIGHT) -> None:
        self.theme_mode     = theme_mode
        self.theme_button   = ft.IconButton(icon=self._get_theme_icon(), on_click=self._toggle_theme, tooltip='Cambiar el tema')
        self.close_button   = ft.IconButton(icon=_close, on_click=self._close_app, tooltip='Cerrar la app')
    
    @property
    def controls(self) -> List[ft.Control]:
        return [self.theme_button, self.close_button]

    def _get_theme_icon(self) -> str:
        return _light_mode if self.theme_mode == ft.ThemeMode.DARK else _dark_mode
    
    def _toggle_theme(self, event: ft.ControlEvent):
        self.theme_mode = ft.ThemeMode.DARK if self.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        self.theme_button.icon = self._get_theme_icon()
        event.page.theme_mode = self.theme_mode
        event.page.update()
    
    def _close_app(self, event: ft.ControlEvent):
        event.page.window_close()
