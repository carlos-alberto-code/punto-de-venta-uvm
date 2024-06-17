import flet as ft


form_shape = ft.Card(
    width=400,
    elevation=10,
)

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    # on_tap=handle_on_tap,
    # on_change=handle_on_change
)
product_list_view = ft.ListView(
    controls=[
        ft.Text(f"Product {i}") for i in range(500)
    ],
    spacing=10,
)

products_shape = ft.Column(
    controls=[
        searcher,
        product_list_view
    ],
    spacing=20,
)

shape = ft.Row(
    controls=[
        form_shape,
        products_shape
    ],
    expand=True,
)