import flet as ft
from datetime import datetime as dt


class WidgetItemCard(ft.Card): # Componente que muestra detalles de un producto
    # Hay que diseñar para que se determine la implementación específica para cada WidgetItemList
    def __init__(self):
        super().__init__()
        self.content = ft.Container(
            content=ft.ListTile(

            )
        )


class ItemsSet(set[WidgetItemCard]): # Gestiona los WidgetItem que se mostrarán en el WidgetItemList
    # Se establece set para que no permita elementos duplicados

    def __init__(self):
        super().__init__()

    def add_item(self, item: WidgetItemCard):
        self.add(item)
    
    def remove_item(self, item: WidgetItemCard):
        self.remove(item)
    
    def clear_items(self):
        self.clear()


class WidgetItemList(ft.Card):

    def __init__(self, title: str):
        super().__init__(elevation=10, expand=True, width=350,)

        self._title = ft.Row([ft.Text(title, size=21)], alignment=ft.MainAxisAlignment.CENTER)
        self._date = ft.Row([ft.Text(f'{dt.now().date()}')], alignment=ft.MainAxisAlignment.CENTER)
        self.top_controls = [self._title, self._date, ft.Divider()]

        self._total_text = ft.Row(
            [ft.Text(f'Total: ${0:,.2f} MXN', size=16)],
            alignment=ft.MainAxisAlignment.CENTER
        )
        self._action_buttons = ft.Row(
            [ft.ElevatedButton('Limpiar'), ft.ElevatedButton('Procesar')], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        self.bottom_controls = [self._total_text, self._action_buttons]

        self.item_set = ItemsSet()
        self.middle_controls = [self._build_middle_controls()]
        self.content = self._build_content()

    def add_widget_item(self, widget_item: WidgetItemCard):
        self.item_set.add_item(widget_item)
        self.content = self._build_content()
        self.update()

    def remove_widget_item(self, widget_item: WidgetItemCard):
        self.item_set.remove_item(widget_item)
        self.content = self._build_content()
        self.update()

    def clear_widget_items(self):
        self.item_set.clear_items()
        self.content = self._build_content()
        self.update()
    
    def _build_middle_controls(self):
        return ft.ListView(
            controls=[
                *self.item_set,
            ],
            padding=10,
            spacing=10,
            expand=True
        )
    
    def _build_content(self):
        return ft.Container(
            content=ft.Column(
                [
                    *self.top_controls,
                    *self.middle_controls,
                    *self.bottom_controls
                ],
            ),
            padding=15,
        )
    