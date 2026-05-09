class Sala:
    def __init__(self, numero_sala: str, capacidade_total: int):
        self.numero_sala = numero_sala
        self.capacidade_total = capacidade_total

    def __str__(self):
        return f"Sala {self.numero_sala} (Capacidade: {self.capacidade_total})"