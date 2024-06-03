import flet as ft
from interfaces.interfaces import ControllerInterface as Controller


product_properties = ('unit', 'category', 'brand', 'quantity', 'cost', 'sell', 'reorder')

class FormEventHandler:

    def __init__(self, controller: Controller, form) -> None:
        self.controller = controller
        self.form = form

    def save(self, event):
        data = event.control.data
        if not data:
            raise ValueError('No data was provided')
        if not all(data.get(prop) for prop in product_properties):
            raise AttributeError('Keys in data are not the same as product properties')
        self.controller.insert(
            unit_id=data['unit'],
            category_id=data['category'],
            brand_id=data['brand'],
            quantity=data['quantity'],
            cost_price=data['cost'],
            selling_price=data['sell'],
            reorder_level=data['reorder'],
        )
        self.clean(event)
        self.cancel(event)
        self.send_message(event)
    
    def cancel(self, event):
        self.form.reset()
        event.page.dialog.open = False
        event.page.update()
    
    def clean(self, event):
        self.form.reset()
        self.form.update()

    def send_message(self, event):
        alert_message = ft.AlertDialog(
            title=ft.Text('Producto agregado'),
            content=ft.Text('El producto ha sido agregado exitosamente'),
            actions=[
                ft.ElevatedButton(text='Ok', on_click=self.cancel)
            ]
        )
        event.page.dialog = alert_message
        event.page.dialog.open = True
        event.page.update()
