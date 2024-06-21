import flet as ft
from components.counters import FloatCounters

def main(page: ft.Page):
    page.add(FloatCounters())
ft.app(main)