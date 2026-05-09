class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    def getNumero(self):
        return self.numero
    
    def getCapacidade(self):
        return self.capacidade
    
    def isReservada(self):
        return self.reservada

class Labortorio(Sala):
    def __init__(self, numero, capacidade):
        super().__init__(numero, capacidade)

    def getTipo(self):
        return "Laboratório"
    
    
class EstudoIndividual(Sala):
    def __init__(self, numero, capacidade):
        super().__init__(numero, capacidade)

    def getTipo(self):
        return "Estudo Individual"
    

class EstudoGrupo(Sala):
    def __init__(self, numero, capacidade):
        super().__init__(numero, capacidade)

    def getTipo(self):
        return "Estudo em Grupo"
    
