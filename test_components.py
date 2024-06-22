import flet as ft
from components.searchers import SearcherTapLess


def main(page: ft.Page):
    
    page.add(SearcherTapLess())


ft.app(main)