import flet as ft

from views.theme.theme_config import ThemeMode, LightTheme, DarkTheme

def main(page: ft.Page):

    # page.window_title_bar_hidden = True
    page.theme = DarkTheme
    page.theme_mode = ft.ThemeMode.DARK

    # Prubeas del contador con herencia
    from views.components.strategy import Counter, IntCounterStrategy, FloatCounterStrategy
    cont = Counter(FloatCounterStrategy())
    page.add(cont)
    


ft.app(target=main)
