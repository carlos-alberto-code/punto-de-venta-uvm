import flet as ft
from time import sleep
from page.components.interfaces.observer_interface import Observer, Subject
from page.components.interfaces.filter_interface import IFilter

class SearcherResult(Subject, ft.Card):

    def __init__(self, model_instance, observer: Observer):
        super().__init__()
        self._observers: list[Observer] = []
        self.attach(observer)
        self.model_instance = model_instance
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
                    ft.Text(value=f'{model_instance.name}'),
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            on_click=self.notify,
        )
    
    def attach(self, observer: Observer):
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.sync(self)


class Searcher(Observer, ft.SearchBar):

    def __init__(self, name: str, model: IFilter):
        super().__init__()
        self.width = 300
        self.height = 30
        self.bar_leading = ft.Row([ft.Icon(str(ft.icons.SEARCH)), ft.Text(f'{name}:')])
        self.view_leading = ft.Row([ft.Icon(str(ft.icons.ARROW_RIGHT)), ft.Text(f'{name}:')])
        self.view_trailing = [ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda _: self.close_view(''))]
        self.model = model
        self.current_model_instance_id = 0
        self.controls = [
            SearcherResult(model_instance=instance, observer=self)
            for instance in self.model.get_all()
        ]
        self.on_change = self.update_results
    
    def sync(self, subject: SearcherResult):
        self.current_model_instance_id = subject.model_instance.id
        self.bar_leading.controls[1].color = ft.colors.PRIMARY # type: ignore
        self.close_view(str(subject.model_instance.name.capitalize()))
    
    def update_results(self, event):
        self.close_view(event.data)
        sleep(0.01)
        results = self.model.search(event.data)
        new_controls = [
            SearcherResult(model_instance=instance, observer=self)
            for instance in results
        ]
        self.controls = [
            *new_controls,
            ft.ElevatedButton(text='Nuevo', icon=ft.icons.ADD)
        ]
        self.open_view()
