from abc import ABC, abstractmethod
from sala import Laboratorio, EstudoIndividual, EstudoEmGrupo

class SalaFactory(ABC):
    @abstractmethod
    def criar_sala(self, numero: str, **kwargs):
        pass

class LaboratorioFactory(SalaFactory):
    def criar_sala(self, numero: str, capacidade: int = 30, equipamentos: list = None):
        return Laboratorio(numero, capacidade, equipamentos or [])

class EstudoIndividualFactory(SalaFactory):
    def criar_sala(self, numero: str, equipamentos: list = None):
        return EstudoIndividual(numero, equipamentos or [])

class EstudoEmGrupoFactory(SalaFactory):
    def criar_sala(self, numero: str, capacidade: int = 6, mesas: int = 1, quadros: int = 1):
        return EstudoEmGrupo(numero, capacidade, mesas, quadros)