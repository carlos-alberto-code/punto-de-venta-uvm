from ..navigation.builder import Module, Section
from .content.customers.customers_section import CustomerSection

import flet as ft

Module(
    'Clientes',
    ft.icons.PEOPLE,
    Section('Clientes', ft.icons.PERSON, CustomerSection)
)

# TODO: Eliminar el módulo de consumidor y todas las carpetas: Firmado: 2024-04-17