from gerenciador_reservas import GerenciadorDeReservas
from reserva_factory import ReservaFactory

class ReservaProxy:

    limite_reservas = 3

    def __init__ (self):
        self.reservas = []

    @classmethod
    def criar_reserva (cls, usuario, sala, inicio, fim):
        gerenciador = GerenciadorDeReservas.get_instancia()

        reservas_ativas = [
            r for r in gerenciador.reservas
            if r.usuario == usuario and r.status == "Confirmada"
        ]

        if len(reservas_ativas) >= cls.limite_reservas:
            print(f"Limite de reservas (3) para {usuario.nome} atingido!")
            return None
        
        return ReservaFactory.criar_reserva(usuario, sala, inicio, fim)