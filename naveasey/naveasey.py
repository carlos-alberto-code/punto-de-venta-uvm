import flet as ft


class Module(ft.NavigationRailDestination):
    """
    La clase ``Module`` representa un módulo (mostrado en la lateral) de la aplicación y proporciona mecanismo para asociar un contenido a dicho módulo que pueda ser gestionado cuando ocurre el evento de cambio de módulo.
    La clase ``Module`` hereda de ``ft.NavigationRailDestination``, por lo que se puede usar como destino de un ``ft.NavigationRail``.

    ## Interfaces públicas:
    - ``name``: El nombre del módulo.
    - ``content``: El contenido del módulo.
    
    Sólo se puede acceder a estas propiedades una vez que se ha creado una instancia de la clase. No está permitido modificarlas.

    ## Ejemplo de uso:

    ``` python
    import flet as ft
    module = Module(name="Inventario", icon=ft.icons.INVENTORY, content=ft.Text(value="Inventario de productos"))
    module.name  # Devuelve "Módulo 1"
    module.content  # Devuelve el contenido asociado al módulo
    ```

    Es preferible usar un ``ft.Column`` o ``ft.Row`` como contenido del módulo para poder mostrar varios controles en el módulo. Pues estos controles permiten anidar y alinear otros controles de manera más sencilla. Una alternativa para cuando alguno de estos controles no está funcionando como se espera, es usar un ``ft.ResponsiveRow``.

    La clase ``Module`` envuelve el contenido en un ft.Container con un ``padding`` de 15 y un ``col`` de 10.80. Esto es para que el contenido del módulo se vea centrado y con un margen en la parte superior e inferior. Esto se hizo por que se pretende que se use un ft.ResponsiveRow usando las propiedades col para distribuir adecuadamente el contenido en la página.

    ## Variables de clase:
    - ``repo``: Un diccionario que contiene todos los módulos creados. La clave es el nombre del módulo y el valor es la instancia de la clase Module. Se puede acceder a este diccionario para obtener un módulo por su nombre. Esto es principalmente beneficioso a la hora de asignar módulos a un usuario.
    """
    repo: dict[str, 'Module'] = {}

    def __init__(
            self,
            name: str,
            icon: str,
            content: ft.ResponsiveRow | ft.Column | ft.Row
    ):
        super().__init__(
            label_content=ft.Text(value=name, size=12),
            icon=icon,
        )
        self._name = name
        self._content = ft.Container(
            col=10.80,
            padding=15,
            content=content,
        )
        Module.repo[name] = self

    @property
    def name(self):
        return self._name
    
    @property
    def content(self):
        return self._content
    