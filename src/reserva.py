from datetime import datetime
from usuario import Usuario
from sala import Sala
from observer import Subject

class Reserva(Subject):
    def __init__(self, usuario: Usuario, sala: Sala, data_hora_inicio: datetime, data_hora_fim: datetime):
        super().__init__() # Inicializa a lista de observers
        self.usuario = usuario
        self.sala = sala
        self.data_hora_inicio = data_hora_inicio
        self.data_hora_fim = data_hora_fim
        self.status = "Confirmada"
        self.add_observer(self.usuario)

    def modificar_horario(self, novo_inicio: datetime, novo_fim: datetime):
        self.data_hora_inicio = novo_inicio
        self.data_hora_fim = novo_fim

        self.notify_push(
            f"Horário da sala {self.sala.numero_sala} alterado.", 
            {"novo_inicio": novo_inicio.strftime("%d/%m %H:%M"), "novo_fim": novo_fim.strftime("%d/%m %H:%M")}
        )

    def cancelar(self):
        self.status = "Cancelada"
        self.notify_pull()

    def obter_estado(self):
        return {
            "sala": self.sala.numero_sala,
            "status": self.status
        }

    def __str__(self):
        inicio = self.data_hora_inicio.strftime("%d/%m %H:%M")
        return f"Reserva [{self.status}]: {self.sala.numero_sala} por {self.usuario.nome} ({inicio})"