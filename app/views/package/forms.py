from sqlalchemy.orm import DeclarativeMeta
import flet as ft

from dataclasses import dataclass
from typing import List

from controllers.form_controller import FormModelController, ModelAttribute
from views.components.counter import MyCounter


@dataclass
class Conversor:
    TEXT = ('VARCHAR', 'CHAR', )
    NUMERIC = ('INTEGER', 'BIGINT', 'DOUBLE', 'FLOAT')

for i in Conversor.TEXT:
    print(i)


translator = {
    int: MyCounter,
    str: ft.TextField,
    # Para fechas, hay que crear un componente.
}


class _Adapter:
    # Iterar List[ModelAttribute]
    # Cada ModelAttribute es un control de entrada. Se debe saber el tipo de dato
    # para determinar el tipo de control de entrada. Los tipos de dato de un modelo pueden agruparse.
    # Todos los valores numéricos convergen a un control (componente) counter.
    # Se implementan varios tipos de contadores, uno para decimales y otro para enteros.
    #Todos los tipos de dato de texto convergen a un control de campo de texto.

    input_controls = {
        'numeric': [MyCounter, ],
        'text': [ft.TextField, ft.Dropdown]
    }

    def __init__(self, model_attibutes: List[ModelAttribute]) -> None:
        # Configurado sólo para manejo de texto y números
        self._controls: List[ft.Control] = []
        adapter = {
            ('CHAR', 'VARCHAR'): ft.TextField(),
            (int): MyCounter(),
        }
        self.model_attibutes = model_attibutes
    
    @property
    def controls(self):
        return self._controls


class Form(ft.UserControl):
    # Me basaré en el principio de desarrollar lo que es importante, así que no es necesario
    # que este artefacto contenga todas las características, sino sólo las que darán valor inicial.
    # Se deben poder alinear las filas o establecer modos predeterminados para todo el cuerpo
    # Debe poder reordenar las filas
    # De los modelos que son compuestos, como Product, debe sugerir campos que ya
    # existen, en caso de que no existan, debe tener recursión en el registro para
    # registrar esos campos del modelo. Esta característica puede ir después.
    # Pero como idea, puedo comprobar qué campos son FK y sobre estos campos
    # construir el modelo.
    # Cada fila debe poder devolver el valos de los controles que alberga para que al final
    # los valores requeridos para el registro se puedan registrar.
    # La dimensión del formulario debe adaptarse a los controles. Crece si hay muchos 
    # controles, decrece si no hay tantos.
    
    body = {
        'attr_name': ft.Row()
    }
    body['attr_name'].alignment = ft.MainAxisAlignment.CENTER
    def __init__(self, model: DeclarativeMeta) -> None:
        super().__init__()
        self.title = model.__name__
        model_attributes = FormModelController(model).model_attibutes
        self.controls = _Adapter(model_attributes).controls
        
    def build(self):
        return ft.AlertDialog(
            adaptive=True,
            title=ft.Row(
                controls=[
                    ft.Text(f'Registrar {self.title}'),
                    ft.ElevatedButton(text='Limpiar', on_click=lambda _:print('Limpiar'))
                ]
            ),
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            content=ft.Column(
                width=250,
                # height=200,
                controls=[
                    ft.TextField(border_radius=20, scale=0.85),
                    MyCounter(),
                ]
            ),
            actions=[
                ft.ElevatedButton(text='Cancelar', on_click=lambda _:print('Cancelado')),
                ft.ElevatedButton(text='Guardado', on_click=lambda _:print('Guardado')),
            ],
        )
