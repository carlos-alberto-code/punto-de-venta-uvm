"""
Este archivo contiene las clases que representan la estructura de navegación de la aplicación.
Un ``Rail`` es un ``ft.NavigationDestination`` que se usará para representar el módulo en el ``ft.NavigationBar``.
Una ``Section`` es un ``ft.NavigationDrawerDestination`` que se usará para representar una sección del módulo en el ``ft.NavigationDrawer``.

Estos dos elementos deben relacionarse de algún modo para que a la hora de desplazarnos entre los módulos
podamos tener opciones pertenecientes a los objetivos de cada módulo. Para ello se ha creado el ``Module``.

Un ``Module`` es una estructura que nos permitirá relacionar un ``Rail`` con determinadas ``Sections``.
Existirán tantas instanicas de ``Module`` como módulos tenga la aplicación.

---

Prácticas recomendadas:

Nuestro flujo de trabajo actual se trata de que cada uno codifique un módulo de la aplicación.
Para ello, cada uno de los módulos debe ser creado en un archivo o carpeta separada.
Asi será claro que cada uno de los módulos es independiente y no depende de los demás.

Al final, todos los módulos deben ser importados en el archivo ``app/views/modules/create_modules.py``.
De forma que en el archivo ``app/main.py`` llame a la función ``create_modules`` que se encargará de crear
todos los módulos de la aplicación. Será necesario crear un artefacto que cree sólo los módulos
que serán usados para un determinado usuario cuando se mejore la función de permisos.
"""

from typing import List
import flet as ft


class Content(ft.UserControl):

    def __init__(self) -> None:
        super().__init__()
    
    def build(self) -> ft.Row:
        pass
        return ft.Row()


class Section(ft.UserControl):
    """
    Una sección es sólo una opción en un menú de navegación en forma de ``ft.NavigationDrawer``.
    Los módulos tienen diferentes secciones que representan las funcionalidades para las que cada módulo
    y sus secciones a sido diseñadas.

    Aunque se pueden crear variables para representar las secciones, es recomendable usar la clase ``Section``
    dentro del objeto ``Module`` para que sea más claro que se está creando una sección para un módulo. Es
    un estilo declarativo en el que es fácil ver que un módulo tiene nombre, icono y secciones.
    """
    
    def __init__(self, name: str, icon: str, content: ft.Column = ft.Column(controls=[ft.Text('None')])) -> None:
        super().__init__()
        self._name = name
        self._icon = icon
        self._content = content
    
    @property
    def name(self) -> str:
        return self._name
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name})'
    
    def build(self) -> ft.NavigationDrawerDestination:
        return ft.NavigationDrawerDestination(
            label=self._name,
            icon=self._icon,
        )


class Rail(ft.UserControl):

    def __init__(self, name: str, icon: str) -> None:
        super().__init__()
        self._name = name
        self._icon = icon
    
    
    def build(self) -> ft.NavigationDestination:
        return ft.NavigationDestination(
            label=self._name,
            icon=self._icon,
        )


class Module:
    """
    Este código representa un módulo en la aplicación.

    ### Argumentos

    - ``name (str)``: El nombre del módulo.
    - ``icon (str)``: El ícono que represent
    - ``sections (List[Section])``: Las secciones que pertenecen al módulo.

    ### Propiedades

    - ``name (str)``: El nombre del módulo.
    - ``rail (Rail)``: El ``Rail`` que representa el módulo en el ``ft.NavigationBar``.
    - ``sections (List[Section])``: Las secciones que pertenecen al módulo.

    Podemos acceder a las propiedades con el uso de @property como accesores.
    Para renderizar el ``Rail`` deberemos llamar al método ``build`` de la clase ``Rail``.
    De esta forma podremos usarlo en el ``ft.NavigationBar``.

    En el caso de la lista de secciones, tendremos que iterar primeramente la lista de 
    secciones del módulo y llamar al método ``build`` de cada una de las secciones.
    Es preferible usar comprensión de listas para este propósito.

    ``[section.build() for section in module.sections]``

    ### Declaración de módulos 

    Para lograr la modularidad en una aplicación, es importante separar los módulos en archivos separados 
    donde podamos identificar claramente que estamos creando un módulo con ciertas secciones para la aplicación.
    Podemos declarar esta intención de la siguiente manera:

    ```python

    PurchaseModule = Module(
        'Compras',
        ft.icons.SHOP,
        Section('Compras', ft.icons.SHOPPING_CART),
        Section('Inventario', ft.icons.INVENTORY),
        Section('Proveedores', ft.icons.PEOPLE),
    )
    ```
    """

    def __init__(self, name: str, icon: str, *sections: Section) -> None:
        self._name = name
        self._rail = Rail(name, icon)
        self._sections = list(sections)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def rail(self) -> Rail:
        return self._rail
    
    @property
    def sections(self) -> List[Section]:
        return self._sections
    
    def __repr__(self) -> str:
        return f'Module(name={self.name}, sections={self._sections})'
