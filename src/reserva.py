from datetime import datetime
from usuario import Usuario
from sala import Sala

class Reserva:
    def __init__(self, usuario: Usuario, sala: Sala, data_hora_inicio: datetime, data_hora_fim: datetime):
        self.usuario = usuario
        self.sala = sala
        self.data_hora_inicio = data_hora_inicio
        self.data_hora_fim = data_hora_fim
        
    def __str__(self):
        inicio_formatado = self.data_hora_inicio.strftime("%d/%m/%Y %H:%M")
        fim_formatado = self.data_hora_fim.strftime("%H:%M")
        return f"Reserva: {self.sala.numero_sala} por {self.usuario.nome} ({inicio_formatado} as {fim_formatado})"