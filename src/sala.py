from abc import ABC, abstractmethod

class Sala(ABC):
    def __init__(self, numero_sala: str, capacidade_total: int):
        self.numero_sala = numero_sala
        self.capacidade_total = capacidade_total

    @abstractmethod
    def obter_detalhes(self) -> str:
        pass
    def __str__(self):
        return f"Sala {self.numero_sala} (Capacidade: {self.capacidade_total})"

class Laboratorio(Sala):
    def __init__(self, numero_sala: str, capacidade_total: int, equipamentos: list):
        super().__init__(numero_sala, capacidade_total)
        self.equipamentos = equipamentos

    def obter_detalhes(self) -> str:
        lista_equip = ", ".join(self.equipamentos) if self.equipamentos else "Nenhum"
        return f"Laboratório, Equipamentos: {lista_equip}"
    
class EstudoIndividual(Sala):
    def __init__(self, numero_sala: str, equipamentos: list = None):
        super().__init__(numero_sala, capacidade_total=1)
        self.equipamentos = equipamentos if equipamentos else []

    def obter_detalhes(self) -> str:
        return "Estudo Individual"
    
class EstudoEmGrupo(Sala):
    def __init__(self, numero_sala: str, capacidade_total: int, quantidade_mesas: int, quantidade_quadros: int):
        super().__init__(numero_sala, capacidade_total)
        self.quantidade_mesas = quantidade_mesas
        self.quantidade_quadros = quantidade_quadros

    def obter_detalhes(self) -> str:
        return f"Estudo em Grupo, {self.quantidade_mesas} Mesas, {self.quantidade_quadros} Quadros"