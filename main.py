from views.theme.theme_config import ThemeMode
import flet as ft



def main(page: ft.Page):

    page.add(ThemeMode(page))
    
ft.app(main)
