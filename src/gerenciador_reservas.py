import threading

class GerenciadorDeReservas:
    _instancia = None
    _lock = threading.Lock()

    def __init__(self):
        if GerenciadorDeReservas._instancia is not None:
            raise Exception("Erro: O Gerenciador é um Singleton. Use GerenciadorDeReservas.get_instancia()")
        
        self.reservas = [] # lista global

    @classmethod
    def get_instancia(cls):
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = GerenciadorDeReservas()
        return cls._instancia

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

    def remover_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)

    def obter_todas_reservas(self):
        return self.reservas

    def obter_reservas_por_sala(self, numero_sala: str):
        return [r for r in self.reservas if r.sala.numero_sala == numero_sala and r.status == "Confirmada"]