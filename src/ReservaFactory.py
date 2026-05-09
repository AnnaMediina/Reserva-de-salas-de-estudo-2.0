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
        """Permite trocar a política em tempo de execução"""
        cls._politica_atual = nova_politica

    @classmethod
    def criar_reserva(cls, usuario: Usuario, sala: Sala, inicio: datetime, fim: datetime):
        tem_conflito = cls._politica_atual.verificar_conflito(sala, usuario, inicio, fim)
        
        if tem_conflito:
            print(" Falha ao criar reserva devido a conflito de horário.\n")
            return None
        
        
        
        nova_reserva = Reserva(usuario, sala, inicio, fim)
        GerenciadorDeReservas().adicionar_reserva(nova_reserva)
        print(f"reserva criada com sucesso para {usuario.nome}.")
        return nova_reserva