from abc import ABC, abstractmethod

class Sala(ABC):
    def __init__(self, numero_sala: str, capacidade_total: int):
        self.numero_sala = numero_sala
        self.capacidade_total = capacidade_total

    @abstractmethod
    def obter_detalhes(self) -> str:
        pass
    def __str__(self):
        return f"Sala {self.numero_sala} (Capacidade: {self.capacidade_total})"