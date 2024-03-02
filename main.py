import flet as ft

from views.color_palette import ColorPalette
from views.logging import LoggingView


def main(page: ft.Page):

    log = LoggingView(page, color_palette=ColorPalette())
    page.add(log)
    
    


ft.app(main)
