class Subject:
    def __init__(self):
        self.observers = []

    def adicionaObservador(self, observer):
        self.observers.append(observer)

    def removeObservador(self, observer):
        self.observers.remove(observer)

    def notificaObservadores(self, sala, acao):
        for observer in self.observers:
            observer.update(sala, acao)


class Observer:
    def update(self, sala, acao):
        pass