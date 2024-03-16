import flet as ft

from views.theme.theme_config import LightTheme, DarkTheme
from app.views.modules.view_template import SectionView

from views.components.navs import Sidebar
from views.modules.modules import ModuleView

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme
    page.bgcolor = LightTheme.color_scheme.background # type: ignore
    page.adaptive = True
    
    section = SectionView(page)
    section.sections.append(ft.NavigationDrawerDestination(icon=ft.icons.SHOP, label='Compras'))
    section.sections.append(ft.NavigationDrawerDestination(icon=ft.icons.SHIELD, label='Proveedores'))
    section.modules.append(ft.NavigationDestination(icon=ft.icons.SHOP, label='Compras'))
    section.modules.append(ft.NavigationDestination(icon=ft.icons.SHIELD, label='Proveedores'))
    page.views.append(section.build())
    
    page.update()

    

ft.app(target=main)
