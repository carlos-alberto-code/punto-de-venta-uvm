import flet as ft


class Counter(ft.UserControl):
    # TODO: Restringir para que no halla valores negativos

    def __init__(self):
        super().__init__()
        self.minus_button = ft.IconButton(icon=ft.icons.REMOVE, on_click=self._minus)
        self.quantity_field = ft.TextField(
            input_filter=ft.NumbersOnlyInputFilter(),
            text_vertical_align=ft.VerticalAlignment.CENTER,
            border=ft.InputBorder.NONE,
            height=40,
            value="0",
            text_align=ft.TextAlign.CENTER, 
            width=50,
        )
        self.add_button = ft.IconButton(icon=ft.icons.ADD, on_click=self._add)
    
    def _minus(self, e):
        valor_actual = int(self.quantity_field.value) # type: ignore
        valor_actual -= 1
        self.quantity_field.value = str(valor_actual)
        self.update()
    
    def _add(self, e):
        valor_actual = int(self.quantity_field.value) # type: ignore
        valor_actual += 1
        self.quantity_field.value = str(valor_actual)
        self.update()
    
    def build(self):
        return ft.Container(
            # border_radius=12,
            # width=180,
            # bgcolor='blue',
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.minus_button, self.quantity_field, self.add_button
                ]
            )
        )