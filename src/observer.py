from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update_push(self, mensagem: str, dados: dict = None):
        pass
    @abstractmethod
    def update_pull(self, subject):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def rmv_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_push(self, mensagem: str, dados: dict = None):
        for observer in self._observers:
            observer.update_push(mensagem, dados)

    def notify_pull(self):
        for observer in self._observers:
            observer.update_pull(self)