from ..packages.NavEase.module import Module, Section

import flet as ft


# TODO: Debo experimentar si la construcción del contenido es suficiente en un archivo para todas las secciones
# Otra forma de hacerlo es seguir el patrón de declaración que hice en los modelos.
# Declaro todos los modelos como SQLAlchemy.

# TODO: Para relacionar una sección con su contenido, voy a aplicar el patrón que use para
# relacionar el rail con su lista de secciones.

PurchaseModule = Module(
    'Compras',
    ft.icons.SHOP,
    Section('Compras', ft.icons.SHOPPING_CART),
    Section('Inventario', ft.icons.INVENTORY),
    Section('Proveedores', ft.icons.PEOPLE),
)

InventoryModule = Module(
    'Inventario',
    ft.icons.INVENTORY,
    Section('Productos', ft.icons.ARTICLE),
    Section('Categorías', ft.icons.TAG),
    Section('Stock mínimo', ft.icons.PRODUCTION_QUANTITY_LIMITS),
)

CustomersModule = Module(
    'Clientes',
    ft.icons.PEOPLE,
    Section('Clientes', ft.icons.PEOPLE),
    Section('Grupos', ft.icons.GROUP),
    Section('Descuentos', ft.icons.DISCOUNT),
)