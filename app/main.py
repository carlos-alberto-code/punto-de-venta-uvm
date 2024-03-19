import flet as ft

from views.modules.navigation_structure import Rail, Section, Module, create_modules # Navegación
from views.theme.theme_config import LightTheme, DarkTheme # Tema
from views.modules.view_template import ViewTemplate # Vista


def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = LightTheme.color_scheme.background # type: ignore
    
    modules = create_modules()

    # Creación de la vista
    prueba_vista = ViewTemplate(
        page=page,
        modules=modules
    )

    # prueba_vista.get_destination_name()

    page.views.append(prueba_vista.build())
    
    
    page.update()

    

ft.app(target=main)
