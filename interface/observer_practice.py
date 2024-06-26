import flet as ft
from purchase_view.context import shape
from purchase_view.ItemList import PurchaseList
from business_classes.Product import Product as Product


from interface.single_observer import SingleObserver, Subject


class TextOne(ft.TextField, Subject):

    def __init__(self):
        super().__init__()
        Subject.__init__(self)
        self.input_filter = ft.NumbersOnlyInputFilter()
        self.data = 0
        self.value = f'{self.data}'
        self.autofocus = True
        self.on_change = self.handle_on_change

    def handle_on_change(self, event):
        self.data = event.control.value
        self.inform_observers()

    def subscribe_observer(self, observer: SingleObserver):
        self.observers.append(observer)

    def unsubscribe_observer(self, observer: SingleObserver):
        self.observers.remove(observer)

    def inform_observers(self):
        for observer in self.observers:
            observer.synchronize(self)


class TextTwo(ft.TextField, Subject):

    def __init__(self):
        super().__init__()
        Subject.__init__(self)
        self.input_filter = ft.NumbersOnlyInputFilter()
        self.data = 0
        self.value = f'{self.data}'
        self.on_change = self.handle_on_change

    def handle_on_change(self, event):
        self.data = event.control.value
        self.inform_observers()

    def subscribe_observer(self, observer: SingleObserver):
        self.observers.append(observer)

    def unsubscribe_observer(self, observer: SingleObserver):
        self.observers.remove(observer)

    def inform_observers(self):
        for observer in self.observers:
            observer.synchronize(self)

class TextThree(ft.TextField, Subject):

    def __init__(self):
        super().__init__()
        Subject.__init__(self)
        self.input_filter = ft.NumbersOnlyInputFilter()
        self.data = 0
        self.value = f'{self.data}'
        self.on_change = self.handle_on_change

    def handle_on_change(self, event):
        self.data = event.control.value
        self.inform_observers()

    def subscribe_observer(self, observer: SingleObserver):
        self.observers.append(observer)

    def unsubscribe_observer(self, observer: SingleObserver):
        self.observers.remove(observer)

    def inform_observers(self):
        for observer in self.observers:
            observer.synchronize(self)


class TextSum(ft.Text, SingleObserver):
    
    def __init__(self):
        super().__init__()
        SingleObserver.__init__(self)
        self.subjects = []
        self.data = 0
        self.value = f'{self.data}'

    def synchronize(self, subject: Subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
        self.data = sum(float(sub.data) for sub in self.subjects)
        self.value = f'${self.data:,.2f} MXN'
        self.update()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    t1 = TextOne()
    t2 = TextTwo()
    t3 = TextThree()
    tsum = TextSum()
    t1.subscribe_observer(tsum)
    t2.subscribe_observer(tsum)
    t3.subscribe_observer(tsum)
    page.add(ft.Column([t1, t2, t3, tsum], alignment=ft.MainAxisAlignment.CENTER))


ft.app(main)