from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def synchronize(self, subject: 'Subject'):
        pass


class Subject(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.observers: list[Observer] = []

    @abstractmethod
    def subscribe_observer(self, observer: Observer):
        self.observers.append(observer)

    @abstractmethod
    def unsubscribe_observer(self, observer: Observer):
        self.observers.remove(observer)

    @abstractmethod
    def inform_observers(self):
        for observer in self.observers:
            observer.synchronize(self)
