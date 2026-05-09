class GerenciadorReservas:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.reservas = []

    
    def adicionarReserva(self, reserva):
        # implementar a lógica
        return
        
        
    def removerReserva(self, reserva):
        # implementar a lógica
        return

    def listarReservasConfirmadas(self):
        reservasConfirmadas = []
        if not self.reservas:
            print("Nenhuma reserva encontrada.")
        else:
            for reserva in self.reservas:
                if reserva.getStatus() == "Confirmado":
                    reservasConfirmadas.append(reserva)
        return reservasConfirmadas

    def modificarReserva(self, reserva, nova_data, nova_hora_inicio, nova_hora_fim):
        reserva.modificarReserva(nova_data, nova_hora_inicio, nova_hora_fim)

    def cancelarReserva(self, reserva):
        self.reservas.remove(reserva)
        reserva.cancelarReserva()

    

    