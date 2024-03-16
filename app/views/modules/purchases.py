# purchase.py

# Este módulo contiene las secciones de la vista de compras que se ubican en el NavigationDrawer.
# Las secciones son controles que permiten el clickeo y la navegación a otras vistas del mismo módulo.
# Este enfoue permite separa las vistas del módulo de compras de las vistas de otros módulos.
# Cuando sean necesarios cambios en las vistas de compras, se podrán realizar sin afectar otras partes del sistema.
# Ademas podremos ir a cada archivo y dar mantenimiento a cada vista de forma independiente.
# Un módulo (destination) está fuertemente relacionado con las secciones del NavigationDrawer.

# El módulo de compras tiene tres secciones:
# 1. Compras
# 2. Inventario
# 3. Proveedores
# Cada sección es una vista. Así que, todo está fuertemente relacionado.

import flet as ft

from view_template import SectionView


module = ft.NavigationDestination(icon=ft.icons.SHOP, label='Compras')

sections = { # Son los controles que se muestran en el NavigationDrawer
    # Asignarun índice a cada control, me permitirá ordenarlos en el NavigationDrawer
    0: ft.NavigationDrawerDestination(icon=ft.icons.SHOP, label='Compras'),
    1: ft.NavigationDrawerDestination(icon=ft.icons.INVENTORY, label='Inventario'),
    2: ft.NavigationDrawerDestination(icon=ft.icons.SHIELD, label='Proveedores'),
}

# def create_views_of_purchases(page: ft.Page):
#     purchase_view = SectionView(page)

#     # Aquí puedes agregar el código adicional para renderizar la vista de compras

#     return purchase_view
