import flet as ft

from views.modules.navigation_structure import Rail, Section # Navegación
from views.theme.theme_config import LightTheme, DarkTheme # Tema
from views.modules.view_template import ViewTemplate # Vista


def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = LightTheme.color_scheme.background # type: ignore
    
    # Creación de módulos
    # Los módulos no deben construir la vista, esta se construirá dentro del ViewTemplate
    sale_rail       = Rail(name='Ventas', icon=ft.icons.APP_REGISTRATION_ROUNDED)
    purchase_rail   = Rail(name='Compras', icon=ft.icons.SHOPPING_BAG)
    inventory_rail  = Rail(name='Inventario', icon=ft.icons.INVENTORY)
    supplier_rail   = Rail(name='Proveedores', icon=ft.icons.PEOPLE)
    customer_rail   = Rail(name='Clientes', icon=ft.icons.PEOPLE)

    # Sección de ventas
    sale_section = Section(name='Secciones de ventas', icon=ft.icons.APP_REGISTRATION_ROUNDED, rail=sale_rail)

    # Sección de compras
    purchase_section = Section(name='Secciones de compras', icon=ft.icons.SHOPPING_BAG, rail=purchase_rail)
    suppliers_section = Section(name='Secciones de proveedores', icon=ft.icons.PEOPLE, rail=purchase_rail)
    


    # Ordenamiento de rieles
    modules = {
        0: sale_rail,
        1: purchase_rail,
        2: inventory_rail,
        3: supplier_rail,
        4: customer_rail,
    }

    # Creación de la vista
    prueba_vista = ViewTemplate(
        page=page,
        modules=modules
    )

    # prueba_vista.get_destination_name()

    page.views.append(prueba_vista.build())
    
    
    page.update()

    

ft.app(target=main)
