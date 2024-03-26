import flet as ft

from view.navigation.appbar_controls import theme_button, close_button
# from view.modules.modules_declaration import module

def main(page: ft.Page):

    # Set the initial theme based on user preference
    page.theme_mode = ft.ThemeMode.DARK  # This should be replaced with the user's preferred theme

    page.theme_mode = page.session.get('theme_mode')
    theme_button.icon = ft.icons.LIGHT_MODE if page.theme_mode == ft.ThemeMode.DARK else ft.icons.DARK_MODE

    # Appbar
    page.appbar = ft.AppBar(
        title=ft.Text('Appbar title'),
        actions=[
            theme_button,
            close_button
        ]
    )
    page.update()

ft.app(target=main)