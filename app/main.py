import flet as ft

from views.theme.theme_config import LightTheme, DarkTheme
from views.modules.view_purchase import PurchaseView

from views.components.navs import Sidebar

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = LightTheme
    page.bgcolor = LightTheme.color_scheme.background # type: ignore
    page.adaptive = True
    
    page.views.append(PurchaseView(page).build())
    
    page.update()

    

ft.app(target=main)
