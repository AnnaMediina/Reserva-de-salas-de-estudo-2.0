from datetime import datetime
from usuario import Usuario
from sala import Sala
from reserva import Reserva

class ReservaFactory:
    @staticmethod
    def criar_reserva(usuario: Usuario, sala: Sala, inicio: datetime, fim: datetime) -> Reserva:
        nova_reserva = Reserva(usuario, sala, inicio, fim)
        return nova_reserva