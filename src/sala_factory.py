from abc import ABC, abstractmethod
from sala import Laboratorio, EstudoIndividual, EstudoEmGrupo

# a factory da sala cria as salas desejadas, os laboratórios, as de estudos individuais e as de estudo em grupo, com suas respectivas capacidades, e equipamentos.
class SalaFactory(ABC):
    @abstractmethod
    def criar_sala(self, numero: str, **kwargs):
        pass

class LaboratorioFactory(SalaFactory):
    def criar_sala(self, numero: str, capacidade: int = 30, equipamentos: list = None):
        return Laboratorio(numero, capacidade, equipamentos or [])

class EstudoIndividualFactory(SalaFactory):
    def criar_sala(self, numero: str):
        return EstudoIndividual(numero)

class EstudoEmGrupoFactory(SalaFactory):
    def criar_sala(self, numero: str, capacidade: int = 6, mesas: int = 1, quadros: int = 1):
        return EstudoEmGrupo(numero, capacidade, mesas, quadros)
    
