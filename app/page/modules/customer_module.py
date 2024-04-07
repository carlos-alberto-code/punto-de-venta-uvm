from ..navigation.builder import Module, Section
from .content.customers.customers_section import CustomerSection

import flet as ft

Module(
    'Clientes',
    ft.icons.PEOPLE,
    Section('Clientes', ft.icons.PERSON, CustomerSection)
)