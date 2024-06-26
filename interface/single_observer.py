from abc import ABC, abstractmethod

class SingleObserver(ABC):
    @abstractmethod
    def synchronize(self, subject: 'Subject'):
        pass

class Subject(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.observer: SingleObserver

    def subscribe_observer(self, observer: SingleObserver):
        self.observer = observer

    def unsubscribe_observer(self, observer: SingleObserver):
        del self.observer

    def inform_observers(self):
        if self.observer:
            self.observer.synchronize(self)