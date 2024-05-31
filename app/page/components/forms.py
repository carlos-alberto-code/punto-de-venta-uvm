import flet as ft

from interfaces.interfaces import FieldInterface as Field
from interfaces.interfaces import ControllerInterface as Controller


class AlertForm(ft.AlertDialog):

    def __init__(self, title: str, model_controller: Controller, **fields: Field):
        super().__init__(
            title=ft.Text(value=title),
            elevation=20,
            actions=[
                ft.ElevatedButton(text='Cancelar', on_click=self.close_form),
                ft.ElevatedButton(text='Limpiar', on_click=self.clear_fields),
                ft.ElevatedButton(text='Guardar', on_click=self.save),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            scrollable=True,
        )
        self.content = ft.Column(
            controls=[
                item for sublist in [
                    [ft.Text(value=f'{field_name}:'), control]
                    for field_name, control in fields.items()
                ] for item in sublist
            ]
        )
        self.fields = fields
        self.model_controller = model_controller
    
    def close_form(self, event):
        self.open = False
        self.update()
    
    def clear_fields(self, event):
        for field in self.fields.values():
            field.reset()
    
    def save(self, event):
        unit_id=self.fields['Unidad'].data # type: ignore
        print(unit_id)
        