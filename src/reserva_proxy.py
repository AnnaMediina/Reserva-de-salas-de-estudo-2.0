from abc import ABC, abstractmethod
from datetime import datetime
from gerenciador_reservas import GerenciadorDeReservas
from reserva_factory import ReservaFactory
from usuario import Aluno, Professor


class ReservaInterface(ABC):
    @abstractmethod
    def criar_reserva(self, usuario, sala, inicio, fim):
        pass


# ── Objeto Real: faz o trabalho de verdade ───────────────────────────────────
class ReservaReal(ReservaInterface):
    def criar_reserva(self, usuario, sala, inicio, fim):
        return ReservaFactory.criar_reserva(usuario, sala, inicio, fim)


class ReservaProxy(ReservaInterface):
    limite_reservas: int = 3

    # cache compartilhado por toda a classe
    _cache: dict = {}
    _ttl_segundos: int = 60          # tempo de vida de cada entrada

    def __init__(self, reserva_real: ReservaReal):
        self._reserva_real = reserva_real

    @classmethod
    def _cache_valido(cls, chave: str) -> bool:
        if chave not in cls._cache:
            return False
        timestamp, _ = cls._cache[chave]
        return (datetime.now() - timestamp).seconds < cls._ttl_segundos

    @classmethod
    def _salvar_no_cache(cls, chave: str, dados) -> None:
        cls._cache[chave] = (datetime.now(), dados)
        print(f"  [CACHE] Dados salvos → chave: '{chave}'")

    @classmethod
    def _invalidar_cache(cls, chave: str) -> None:
        if chave in cls._cache:
            del cls._cache[chave]
            print(f"  [CACHE] Cache invalidado → chave: '{chave}'")


    def criar_reserva(self, usuario, sala, inicio, fim):
        gerenciador = GerenciadorDeReservas.get_instancia()

        if not isinstance(usuario, (Aluno, Professor)):
            print(f"\n[PROXY] BLOQUEADO: {usuario.nome} (visitante) não pode fazer reservas.")
            return None

        reservas_ativas = [
            r for r in gerenciador.reservas
            if r.usuario == usuario and r.status == "Confirmada"
        ]
        if len(reservas_ativas) >= self.limite_reservas:
            print(f"\n[PROXY] BLOQUEADO: {usuario.nome} já possui "
                f"{self.limite_reservas} reservas ativas.")
            return None

        nova_reserva = self._reserva_real.criar_reserva(usuario, sala, inicio, fim)
        self._invalidar_cache(f"sala_{sala.numero_sala}")
        self._invalidar_cache(f"usuario_{usuario.nome}")

        return nova_reserva

    def cancelar_reserva(self, reserva) -> None:
        reserva.cancelar()                         
        GerenciadorDeReservas.get_instancia().remover_reserva(reserva)

        self._invalidar_cache(f"sala_{reserva.sala.numero_sala}")
        self._invalidar_cache(f"usuario_{reserva.usuario.nome}")

    def modificar_reserva(self, reserva, novo_inicio: datetime, novo_fim: datetime) -> None:
        reserva.modificar_horario(novo_inicio, novo_fim)  # dispara notify_push

        self._invalidar_cache(f"sala_{reserva.sala.numero_sala}")
        self._invalidar_cache(f"usuario_{reserva.usuario.nome}")

    def listar_por_usuario(self, usuario) -> list:
        chave = f"usuario_{usuario.nome}"

        if self._cache_valido(chave):
            _, dados = self._cache[chave]
            print(f"  [CACHE] HIT → usuário '{usuario.nome}' (cache utilizado)")
            return dados

        # cache miss: busca nos dados reais
        print(f"  [CACHE] MISS → usuário '{usuario.nome}' (buscando dados...)")
        gerenciador = GerenciadorDeReservas.get_instancia()
        dados = [r for r in gerenciador.reservas if r.usuario == usuario]

        self._salvar_no_cache(chave, dados)
        return dados

    def listar_por_sala(self, numero_sala: str) -> list:
        chave = f"sala_{numero_sala}"

        if self._cache_valido(chave):
            _, dados = self._cache[chave]
            print(f"  [CACHE] HIT → sala '{numero_sala}' (cache utilizado)")
            return dados

        print(f"  [CACHE] MISS → sala '{numero_sala}' (buscando dados...)")
        gerenciador = GerenciadorDeReservas.get_instancia()
        dados = [r for r in gerenciador.reservas if r.sala.numero_sala == numero_sala]

        self._salvar_no_cache(chave, dados)
        return dados