import flet as ft


def main(page: ft.Page):
    page.add(ft.Text("Hello, World!"))
    page.add(ft.Text("This is a test!"))
    page.add(ft.Text("This is a test!"))

ft.app(main)