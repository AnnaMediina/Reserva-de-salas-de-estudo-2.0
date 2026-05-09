from Observer import Subject

class Reserva(Subject):
    def __init__(self, sala, usuario, data, horaInicio, horaFim):
        super().__init__()
        self.sala = sala
        self.usuario = usuario
        self.data = data
        self.hora_inicio = horaInicio
        self.hora_fim = horaFim
        self.status = "Confirmado"

    def getSala(self):
        return self.sala
    
    def getUsuario(self):
        return self.usuario
    
    def getData(self):
        return self.data
    
    def getHoraInicio(self):
        return self.hora_inicio
    
    def getHoraFim(self):
        return self.hora_fim

    def getStatus(self):
        return self.status
    
    def cancelarReserva(self):
        self.status = "Cancelado"
        self.notificaObservadores(self.sala, "cancelada")

    def modificarReserva(self, nova_data, nova_hora_inicio, nova_hora_fim):
        self.data = nova_data
        self.hora_inicio = nova_hora_inicio
        self.hora_fim = nova_hora_fim
        self.notificaObservadores(self.sala, "modificada")
    
    
