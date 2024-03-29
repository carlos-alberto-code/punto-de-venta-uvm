from .builder import Module, Section
from .content.customers.customers_section import CustomersModule

import flet as ft

Module(
    'Clientes',
    ft.icons.PEOPLE,
    Section('Clientes', ft.icons.PERSON, CustomersModule().build())
)