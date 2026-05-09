from abc import ABC, abstractmethod
from sala import Laboratorio, EstudoIndividual, EstudoEmGrupo

class SalaFactory(ABC):
    @abstractmethod
    def criar_sala(self, numero: str, **kwargs):
        pass