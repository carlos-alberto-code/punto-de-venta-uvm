import flet as ft

from views.theme.theme_config import ThemeMode, LightTheme, DarkTheme

def main(page: ft.Page):

    # page.window_title_bar_hidden = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme
    page.update()

    # Prubeas del contador con herencia
    from views.packages.form.counter import Counter, IntCounter, FloatCounter

    contador = Counter(IntCounter())
    page.add(contador)
    print(contador.value)
    


ft.app(target=main)
