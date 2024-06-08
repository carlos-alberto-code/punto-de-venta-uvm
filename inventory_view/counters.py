import flet as ft
from typing import Optional


class Counter(ft.Card):

    def __init__(
            self,
            width: Optional[int] = 150,
            elevation: Optional[int] = 0,
            start_value: Optional[int] = 1,
            end_value: Optional[int] = 100,
            # step_increment: Optional[int] = 1,
            # negative_values: Optional[bool] = False,
    ):
        super().__init__(
            width=width,
            elevation=elevation,
            # alignment=ft.alignment.center,      
        )
        self._start_value = start_value
        self._end_value = end_value
        # self._step_increment = step_increment
        # self._negative_values = negative_values
        self._txtfld = ft.TextField(
            border=ft.InputBorder.NONE,
            expand=True,
            adaptive=True,
            value=str(start_value),
            text_size=14,
            text_align=ft.TextAlign.CENTER,
            text_vertical_align=ft.VerticalAlignment.START,
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self.content = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.REMOVE,
                    on_click=self.decrement,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)
                    )
                ),
                self._txtfld,
                ft.IconButton(
                    icon=ft.icons.ADD,
                    on_click=self.increment,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10)
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    @property
    def value(self):
        return str(self._txtfld.value)
    
    @value.setter
    def value(self, value: int):
        self._txtfld.value = str(value)

    def increment(self, event):
        if self.value is not None and self._end_value is not None and int(self.value) < int(self._end_value):
            self.value = int(self.value) + 1
        else:
            if self._end_value is not None:
                self.value = int(self._end_value)
        self._txtfld.update()

    def decrement(self, event):
        if self.value is not None and int(self.value) > 0:
            self.value = int(self.value) - 1
        if self.value is not None and self._end_value is not None and int(self.value) > int(self._end_value):
            self.value = int(self._end_value)
        self._txtfld.update()