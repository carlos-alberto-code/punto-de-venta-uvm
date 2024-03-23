"""
Cada archivo en esta carpeta declara el contenido de las secciones de un módulo.
Aquí declaramos el contenido de todas las secciones del módulo de compras.
Todo el contenido debe implementarse en un ft.Column para que se pueda inyectar en los 
objetos Section. No es necesario hacerlo como variable, puede crearse una clase que
implemenete el método build y devuelva el contenido de la sección en forma de ft.Column.
"""

import flet as ft


purchase_content = ft.Column(
    controls=[
        ft.Text('Compras'),
        ft.ElevatedButton(text='Agregar compra', icon=ft.icons.ADD),
        ft.ElevatedButton(text='Ver compras', icon=ft.icons.LIST),
        
    ]
)

inventory_content = ft.Column(
    controls=[
        ft.Text('Inventario'),
        ft.ElevatedButton(text='inventario', icon=ft.icons.ADD),
        ft.ElevatedButton(text='Ver productos', icon=ft.icons.LIST),
    ]
)

providers_content = ft.Column(
    controls=[
        ft.Text('Proveedores'),
        ft.ElevatedButton(text='Agregar proveedor', icon=ft.icons.ADD),
        ft.ElevatedButton(text='Ver proveedores', icon=ft.icons.LIST),
    ]
)