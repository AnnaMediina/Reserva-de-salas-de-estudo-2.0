from abc import ABC, abstractmethod
from gerenciador_reservas import GerenciadorDeReservas
from reserva_factory import ReservaFactory
from usuario import Aluno, Professor

class ReservaInterface(ABC):
    @abstractmethod
    def criar_reserva(self, usuario, sala, inicio, fim):
        pass

class ReservaReal(ReservaInterface):

    def criar_reserva(self, usuario, sala, inicio, fim):
        return ReservaFactory.criar_reserva(usuario, sala, inicio, fim)
    

class ReservaProxy(ReservaInterface):

    limite_reservas = 3

    def __init__ (self, reserva_real):
        self.reserva_real = reserva_real
        self.reservas = []

    @classmethod
    def criar_reserva (self, usuario, sala, inicio, fim):
        gerenciador = GerenciadorDeReservas.get_instancia() 

        if not isinstance(usuario, (Aluno, Professor)):
            print(f"Usuário {usuario.nome} não tem permissão para fazer reservas.")
            return None
        
        else:
            reservas_ativas = [
                r for r in gerenciador.reservas
                if r.usuario == usuario and r.status == "Confirmada"
            ]

            if len(reservas_ativas) >= self.limite_reservas:
                print(f"Limite de {self.limite_reservas} reservas para {usuario.nome} atingido!")
                return None
            return self.reserva_real.criar_reserva(usuario, sala, inicio, fim)
