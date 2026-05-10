from datetime import datetime
from usuario import Usuario
from sala import Sala
from observer import Subject

# reserva: é o sujeito observado, ela guarda as informações da reserva, como data, hora, sala e usuário. 
class Reserva(Subject):
    def __init__(self, usuario: Usuario, sala: Sala, data: datetime, hora_inicio: datetime, hora_fim: datetime):
        super().__init__() # Inicializa a lista de observers
        self.usuario = usuario
        self.sala = sala
        self.data_reserva = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.status = "Confirmada"
        self.add_observer(self.usuario)

    def modificar_horario(self, novo_inicio: datetime, novo_fim: datetime):
        self.hora_inicio = novo_inicio
        self.hora_fim = novo_fim

        self.notify_push(
            f"Horário da sala {self.sala.numero_sala} alterado.", 
            {"novo_inicio": novo_inicio.strftime("%H:%M"), "novo_fim": novo_fim.strftime("%H:%M")}
        )

    def cancelar(self):
        self.status = "Cancelada"
        self.notify_pull()

    def obter_estado(self):
        return {
            "sala": self.sala.numero_sala,
            "data_reserva": self.data_reserva.strftime("%d/%m/%Y"),
            "hora_inicio": self.hora_inicio.strftime("%H:%M"),
            "hora_fim": self.hora_fim.strftime("%H:%M"),
            "status": self.status
        }

    def __str__(self):
        return f"Reserva [{self.status}]: {self.sala.numero_sala} por {self.usuario.nome}. Data ({self.data_reserva.strftime('%d/%m/%Y')}) - Horário: {self.hora_inicio.strftime('%H:%M')} - {self.hora_fim.strftime('%H:%M')}"