from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def sync(self, subject: 'Subject'):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass