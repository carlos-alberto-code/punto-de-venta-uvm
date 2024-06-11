import flet as ft


section_tabs = ft.Tabs(
    tabs=[
        ft.Tab(
            text='Nueva compra',
            icon=ft.icons.SHOPIFY,
        ),
        ft.Tab(
            text='Historial',
            icon=ft.icons.HISTORY,
        ),
    ],
    tab_alignment=ft.TabAlignment.CENTER,
    scrollable=True,
)