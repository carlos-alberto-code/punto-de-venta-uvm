import flet as ft


class MyCounter(ft.UserControl):
    # TODO: Tener la cualidad de ser sólo entero o permitir puntos decimales (para precios)
    # Crear un Strategy para implementar diferente comportamiento

    def __init__(self):
        super().__init__()
        # Alineación
        self._alignment = ft.MainAxisAlignment.CENTER
        # Botones
        self._minus_button = ft.IconButton(icon=ft.icons.REMOVE, on_click=self._minus)
        self._add_button = ft.IconButton(icon=ft.icons.ADD, on_click=self._add)
        # Campo de texto del componente
        self._quantity_field = ft.TextField(
            text_vertical_align=ft.VerticalAlignment.START,
            text_align=ft.TextAlign.CENTER, 
            input_filter=ft.InputFilter(allow=True, regex_string=r"^[0-9]*$", replacement_string=''),
            border=ft.InputBorder.NONE,
            value="0",
            width=50,
            read_only=True, # Para evitar crear manejo de errores cuando se typea.
        )
        self._row = ft.Row(
            scale=0.9,
            spacing=1,
            alignment=self._alignment,
            controls=[
                self._minus_button, self._quantity_field, self._add_button
            ]
        )
    
    # Alineación del componente

    @property
    def alignment(self):
        self._row.alignment = self._alignment
        return self._alignment
    
    @alignment.setter
    def alignment(self, alignment: ft.MainAxisAlignment):
        self._alignment = alignment
        self._row.alignment = self._alignment

    def _minus(self, e):
        current_value = int(self._quantity_field.value) # type: ignore
        if current_value > 0:
            current_value -= 1
        self._quantity_field.value = str(current_value)
        self.update()
    
    def _add(self, e):
        current_value = int(self._quantity_field.value) # type: ignore
        if current_value < 100:
            current_value += 1
        self._quantity_field.value = str(current_value)
        self.update()
    

    def build(self):
        return self._row
    


"""
from components.counter import Count, IntCount, FloatCount

int_count = Count(IntCount)
float_count = Count(FloatCount)
"""

class CountStrategy:
    pass


class IntCount(CountStrategy):
    """
    Este componente tiene:
        - Dos botones para aumentar o disminuir los enteros.
        - Un campo de texto para mostrar y modificar el valor.
    """
    pass


class FloatCount(CountStrategy):
    '''
    Ideas:
        - Reusar los dos botones para controlar la parte entera y agregar otros dos botones
        para controlar la parte decimal.
        - Heredar los dos botones pero ahora estos controlan la parte decimal.
    '''
    pass


class Count(ft.UserControl):

    def __init__(self, counter_strategy: CountStrategy):
        super().__init__()
        self.counter_strategy = counter_strategy
    
    def build(self):
        return ft.AlertDialog(

        )

"""
Estoy teniendo problemas para identificar si es necesario implementar el patrón Strategy
para crear diferentes Counters; uno para enteros y uno para decimales.

Parte de mi pensamiento dice que un IntCounter 'es un' tipo de Counter, al igual que un FloatCounter
'es un' tipo de Counter, lo cual me dirige rápido hacia la herencia.

Otra parte de mi pensamiento sugiere que, al ser el patrón Strategy un patrón de diseño de comportamiento,
un FloatCounter se comporta diferente que un IntCounter.

La implementación será diferente dependiendo del diseño de estos componentes. Si uso Strategy, debo inyectar
la estrategia en el Counter, mientas que si uso herencia, debo usar la clase específica.

# Strategy
counter = Counter(FloatCounter)

# Herencia
float_counter = FloatCounter()

Por ahora veo la herencia como la solución mas viable ya que aún no entiendo el patrón Strategy completamente


# Usando herencia
Ya que voy a usar la herencia como solución, de las ideas que plantee, si uso sólo dos controles, sobreescribiré
el comportamiento de los botones. Si agrego dos botones más, sólo agrego otro comportamiento.

"""

class Counter(ft.UserControl):

    def __init__(self) -> None:
        super().__init__()
        self.int_minus_button = ft.IconButton()
        self.quantity_field = ft.TextField()
        self.int_add_button = ft.IconButton()
    
    def remove_one(self, e):
        pass

    def add_one(self, e):
        pass


class IntCounter(Counter):
    pass


class FloatCounter(Counter):
    
    def __init__(self) -> None:
        super().__init__()
        self.float_minus_button = ft.IconButton()
        self.quantity_field.value = '0.0'
        self.float_add_button = ft.IconButton()


# Sección de aprendizaje
# Implementaré varios contadores basado en patrones de diseño
# Strategy
# Herencia
# Patrón de estado
# Patrón de decorador
