import flet as ft

from page.components.Counter import Counter
from page.components.search_bar_filter.filter_interface import IFilter



class Results(ft.Card):
    def __init__(self, id:int, text: str, on_click=None) -> None:
        super().__init__()
        self.id = id
        self.text = text
        self.content = ft.Container(
            height=30,
            margin=3,
            padding=ft.Padding(left=10, right=0, top=0, bottom=0),
            alignment=ft.alignment.center,
            ink=True,
            border_radius=10,
            content=ft.Row(
                controls=[
                    ft.Icon(str(ft.icons.CIRCLE), size=10),
                    ft.Text(value=text),
                    ft.Text(value=str(id), visible=False)
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            on_click=on_click,
        )


class ProductPropertySearch(ft.SearchBar):
    def __init__(self, bar_hint_text: str, model: IFilter):
        super().__init__()
        self.width = 300
        self.height = 40
        self.bar_leading = ft.Text(bar_hint_text + ':')
        self.view_leading = ft.Text(bar_hint_text + ':', color=ft.colors.PRIMARY)
        self.bar_trailing = [ft.Icon(str(ft.icons.ARROW_DROP_DOWN_CIRCLE_OUTLINED))]
        self.view_trailing = [ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view())]
        self.model = model
        self.instances = model.get_all()
        self.controls = [
            Results(id=instance.id, text=instance.name, on_click=self.on_click_in_result)
            for instance in self.instances
            # ft.ElevatedButton(text='Nuevo', on_click=lambda _: print('nueva propiedad'))
        ]
        self.controls.append(ft.ElevatedButton(text='Nuevo', on_click=lambda _: print('nueva propiedad'), bgcolor=ft.colors.ON_BACKGROUND, color=ft.colors.BACKGROUND))
        self.controls.append(ft.Container(height=15))
        
    
    def on_click_in_result(self, event):
        value = event.control.content.controls[1].value.capitalize()
        self.bar_leading.color = ft.colors.PRIMARY # type: ignore
        self.view_leading.color = ft.colors.PRIMARY # type: ignore
        self.close_view(text=value)


ft.AlertDialog()
class ProductForm(ft.AlertDialog):

    def __init__(self, **models: IFilter):
        super().__init__()
        self.expandable = True
        self.title = ft.Text('Nuevo producto')
        self.icon = ft.Icon(str(ft.icons.INVENTORY))
        self.scrollable = True
        self.content = ft.Column(
            controls=[
                # Un contenedor para clickear y poder subir una imagen del producto
                ft.Row(
                    [
                        ft.Container(
                            height=100,
                            width=100,
                            margin=10,
                            border=ft.border.all(0.5),
                            border_radius=10,
                            ink=True,
                            alignment=ft.alignment.center,
                            content=ft.Icon(str(ft.icons.IMAGE), size=50),
                            on_click=lambda _: print('Subir imagen'),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ProductPropertySearch(list(models.keys())[0], list(models.values())[0]),
                ProductPropertySearch(list(models.keys())[1], list(models.values())[1]),
                ProductPropertySearch(list(models.keys())[2], list(models.values())[2]),
                ft.Row(
                    [
                        ft.Text('Cantidad:'),
                        Counter(0),
                    ],
                    width=300
                ),
                ft.Row(
                    [
                        ft.Text('Precio de compra:'),
                        Counter(0),
                    ],
                    width=300
                ),
                ft.Row(
                    [
                        ft.Text('Precio de venta:'),
                        Counter(0),
                    ],
                    width=300,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [
                        ft.Text('Existencias mínimas:'),
                        Counter(0),
                    ],
                    width=300
                ),
            ],
        )
        self.actions = [
            ft.ElevatedButton(text='Limpiar', on_click=lambda _: print('Limpiar')),
            ft.ElevatedButton(text='Guardar', on_click=lambda _: print('Guardar')),
        ]
