from ..packages.NavEase.module import Module
from .modules_declaration import (
    PurchaseModule,
    InventoryModule,
    CustomersModule,
)

def create_modules() -> list[Module]:
    return [
        PurchaseModule,
        InventoryModule,
        CustomersModule,
    ]