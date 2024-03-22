"""
En este archivo declaramos todos los módulos que se mostrarán en la aplicación.
La filtración de módulos que dependen de un usuario ocurre en otro lugar. Aquí
hacemos la declaración y los empaquetamos para que puedan intercambiarse en 
tiempo de ejecución
"""

from ..packages.NavEase.module import Module, Section
from ..content.purchase_module import purchase_content, inventory_content, providers_content

from typing import List
import flet as ft


# DECLARACIÓN DE MÓUDLOS

PurchaseModule = Module(
    'Compras',
    ft.icons.SHOP,
    Section(name='Compras', icon=ft.icons.SHOPPING_CART, content=purchase_content),
    Section(name='Inventario', icon=ft.icons.INVENTORY, content=inventory_content),
    Section(name='Proveedores', icon=ft.icons.PEOPLE, content=providers_content),
)

InventoryModule = Module(
    'Inventario',
    ft.icons.INVENTORY,
    Section(name='Productos', icon=ft.icons.ARTICLE),
    Section(name='Categorías', icon=ft.icons.TAG),
    Section(name='Stock mínimo', icon=ft.icons.PRODUCTION_QUANTITY_LIMITS),
)

CustomersModule = Module(
    'Clientes',
    ft.icons.PEOPLE,
    Section(name='Clientes', icon=ft.icons.PEOPLE),
    Section(name='Grupos', icon=ft.icons.GROUP),
    Section(name='Descuentos', icon=ft.icons.DISCOUNT),
)


# CREACIÓN DE MÓDULOS
def create_modules() -> List[Module]:
    """
    Devuelve una lista de módulos.
    Cómo regla, debemos usar como clave el nombre del módulo (``str``)
    y como valor el módulo en sí (``Module``). De esta forma podremos 
    ordenar y localizar los módulos de forma más sencilla.

    ## Implementación

    Se sugiere apegarse a la siguiente forma de desarrollo:
    ```python
    from modules_declaration import (
        PurchaseModule,
        InventoryModule,
        CustomersModule,
    )

    def create_modules() -> List[Module]:
        return [
            PurchaseModule,
            InventoryModule,
            CustomersModule,
        ]
    ```
    """
    return [
        PurchaseModule,
        InventoryModule,
        CustomersModule,
    ]