from ..packages.NavEase.module import Module
from .modules_declaration import (
    PurchaseModule,
    InventoryModule,
    CustomersModule,
)

from typing import List


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
