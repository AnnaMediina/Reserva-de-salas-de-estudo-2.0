from abc import ABC, abstractmethod
from datetime import datetime
from sala import Sala
from usuario import Usuario, Professor
from gerenciador_reservas import GerenciadorDeReservas

class PoliticaDeReserva(ABC):
    @abstractmethod
    def verificar_conflito(self, sala: Sala, usuario: Usuario, inicio: datetime, fim: datetime) -> bool:
        pass

class PoliticaPrimeiroChegar(PoliticaDeReserva):
    def verificar_conflito(self, sala: Sala, usuario: Usuario, inicio: datetime, fim: datetime) -> bool:

        gerenciador = GerenciadorDeReservas.get_instancia()
        reservas_da_sala = gerenciador.obter_reservas_por_sala(sala.numero_sala)
        
        for r in reservas_da_sala:
            if max(inicio, r.data_hora_inicio) < min(fim, r.data_hora_fim):
                print(f"[CONFLITO] A sala {sala.numero_sala} já está ocupada neste horário.")
                return True 
        return False 

class PoliticaPrioridadeDocente(PoliticaDeReserva):
    def verificar_conflito(self, sala: Sala, usuario: Usuario, inicio: datetime, fim: datetime) -> bool:

        gerenciador = GerenciadorDeReservas.get_instancia()
        reservas_da_sala = gerenciador.obter_reservas_por_sala(sala.numero_sala)
        
        for r in reservas_da_sala:
            if max(inicio, r.data_hora_inicio) < min(fim, r.data_hora_fim):
                if isinstance(usuario, Professor) and not isinstance(r.usuario, Professor):
                    print(f"Prioridade do Professor {usuario.nome} sobrepondo reserva de {r.usuario.nome}.")
                    r.cancelar() 
                    gerenciador.remover_reserva(r)
                    return False 
                else:
                    print(f"[CONFLITO] Sala ocupada e sem prioridade suficiente.")
                    return True 
        return False