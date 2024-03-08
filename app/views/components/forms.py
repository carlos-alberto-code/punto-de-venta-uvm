from sqlalchemy.orm import DeclarativeMeta

from typing import List

import flet as ft

from .counter import Counter
from controllers.form_controller import FormModelController, ModelAttribute


class Adapter:

    def __init__(self, model_attibutes: List[ModelAttribute]) -> None:
        self._controls: List[ft.Control] = []
        mapper = {
            int: Counter(),
        }
        model_attibutes = model_attibutes
    
    @property
    def controls(self):
        return self._controls


class Form(ft.UserControl):
    
    def __init__(self, model: DeclarativeMeta) -> None:
        super().__init__()
        self.title = model.__name__
        model_attributes = FormModelController(model).model_attibutes
        self.controls = Adapter(model_attributes).controls
        self.button_save = ft.FilledButton(text='Guardar', on_click=self.guardar)
        self.button_dimiss = ft.FilledButton(text='Cancelar', on_click=self.cancelar)
    
    def cancelar(self, e):
        print('cancelar')
    
    def guardar(self, e):
        print('Guardar')
        
    def build(self):
        return ft.AlertDialog(
            title=ft.Text(f'Registro de {self.title}'), # TODO: Agregar el nombre del formulario en función del nombre del modelo
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                self.button_dimiss,
                self.button_save,
            ],
        )