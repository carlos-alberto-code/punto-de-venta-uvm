import flet as ft


class EditableField(ft.TextField):

    def __init__(self, text_size:int, prefix_text: str, value: float | int, suffix_text: str, input_filter=None, on_change=None, on_submit=None):
        super().__init__()
        self.text_size = text_size
        self.text_align = ft.TextAlign.CENTER
        self.prefix_text = prefix_text
        self.suffix_text = suffix_text
        self.value = f'{value:,.2f}'
        self.border = ft.InputBorder.NONE
        self.width = 200
        if input_filter:
            self.input_filter = ft.InputFilter(regex_string=input_filter)
        self.on_change = on_change
        self.on_submit = on_submit
    
    @property
    def get_value(self):
        return self.value