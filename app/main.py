import flet as ft

from views.theme.theme_config import ThemeMode, LightTheme

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme
    page.scroll =ft.ScrollMode.ADAPTIVE

    # Prubeas de Form
    from views.components.counter import Counter
    from views.components.forms import Form
    from models.models import Category, Brand, Product

    form = Form(Product).build()
    page.dialog = form

    def abrir_formulario(e):
        form.open = True
        page.update()

    page.add(
        ft.FilledButton('Abrir formulario', on_click=abrir_formulario),
        Counter()
    )


ft.app(target=main)
