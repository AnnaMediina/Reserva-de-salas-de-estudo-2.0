from abc import ABC, abstractmethod
from datetime import datetime
from sala import Sala
from usuario import Usuario, Professor
from gerenciador_reservas import GerenciadorDeReservas

# o strategy define qual a politica de agendamento, como o sistema lida com os conflitos de horários e prioridades.
class PoliticaDeReserva(ABC):
    @abstractmethod
    def verificar_conflito(self, sala: Sala, usuario: Usuario, data: datetime, inicio: datetime, fim: datetime) -> bool:
        pass

class PoliticaPrimeiroChegar(PoliticaDeReserva):
    def verificar_conflito(self, sala: Sala, usuario: Usuario, data: datetime, inicio: datetime, fim: datetime) -> bool:

        gerenciador = GerenciadorDeReservas.get_instancia()
        reservas_da_sala = gerenciador.obter_reservas_por_sala(sala.numero_sala)
        
        for reserva in reservas_da_sala:
            if reserva.data_reserva.strftime("%d/%m/%Y") == data.strftime("%d/%m/%Y"):
                if max(inicio, reserva.hora_inicio) < min(fim, reserva.hora_fim):
                    print(f"[CONFLITO] A sala {sala.numero_sala} já está ocupada neste horário por {reserva.usuario.nome}.")
                    return True 
        return False 

class PoliticaPrioridadeDocente(PoliticaDeReserva):
    def verificar_conflito(self, sala: Sala, usuario: Usuario, data: datetime, inicio: datetime, fim: datetime) -> bool:

        gerenciador = GerenciadorDeReservas.get_instancia()
        reservas_da_sala = gerenciador.obter_reservas_por_sala(sala.numero_sala)
        
        for reserva in reservas_da_sala:
            if reserva.data_reserva.strftime("%d/%m/%Y") == data.strftime("%d/%m/%Y"):
                if max(inicio, reserva.hora_inicio) < min(fim, reserva.hora_fim):
                    if isinstance(usuario, Professor) and not isinstance(reserva.usuario, Professor):
                        print(f"Prioridade do Professor {usuario.nome} sobrepondo reserva de {reserva.usuario.nome}.")
                        reserva.cancelar() 
                        gerenciador.remover_reserva(reserva)
                        return False 
                else:
                    print(f"[CONFLITO] Sala ocupada e sem prioridade suficiente.")
                    return True 
        return False