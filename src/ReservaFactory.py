from datetime import datetime
from usuario import Usuario
from sala import Sala
from reserva import Reserva
from estrategia_reserva import PoliticaDeReserva, PoliticaPrimeiroChegar
from gerenciador_reservas import GerenciadorDeReservas

class ReservaFactory:
    _politica_atual = PoliticaPrimeiroChegar()

    @classmethod
    def definir_politica(cls, nova_politica: PoliticaDeReserva):
        cls._politica_atual = nova_politica

    @classmethod
    def criar_reserva(cls, usuario: Usuario, sala: Sala, inicio: datetime, fim: datetime):
        tem_conflito = cls._politica_atual.verificar_conflito(sala, usuario, inicio, fim)
        
        if tem_conflito:
            print(f"Falha ao criar reserva para {usuario.nome} devido a conflito de horário.")
            return None
        nova_reserva = Reserva(usuario, sala, inicio, fim)
        GerenciadorDeReservas.get_instancia().adicionar_reserva(nova_reserva)
        print(f" -> reserva criada com sucesso para {usuario.nome}.")
        return nova_reserva