from observer import Observer

# usuarios: são os observadores, podem ser estudantes, professores, ou visitantes externos. Eles recebem notificações quando suas reservas são modificadas ou canceladas.
class Usuario(Observer):
    def __init__(self, nome: str, vinculo: str):
        self.nome = nome
        self.vinculo = vinculo
        
    # notificações push: são enviadas ativamente para o usuário, com uma mensagem e dados específicos sobre a mudança.
    def update_push(self, msg: str, dados: dict = None):
        print(f"\n[notificacao PUSH enviada para {self.nome} - {self.vinculo}]\n{msg}")
        if dados:
            print(f"-Dados enviados ativamente: {dados}")

    # notificacoes pull: são enviadas quando a reserva foi modificada por conta de outro usuário.
    def update_pull(self, subject):
        print(f"\n[notificacao PULL enviada para {self.nome} -> {self.vinculo}], algo mudou na sua reserva!")
        estado_atual = subject.obter_estado()
        print(f"Status da sua reserva da sala {estado_atual['sala']} é '{estado_atual['status']}'")

    def __str__(self):
        return f"{self.nome} ({self.vinculo})"


class Professor(Usuario):
    def __init__(self, nome: str, identificador: str):
        super().__init__(nome, "Professor")
        self.identificador = identificador

    def __eq__(self, other):
        if not isinstance(other, Professor):
            return False
        return self.identificador == other.identificador

    def __hash__(self):
        return hash(self.identificador)


class Aluno(Usuario):
    def __init__(self, nome: str, matricula: str):
        super().__init__(nome, "Aluno")
        self.matricula = matricula

    def __eq__(self, other):
        if not isinstance(other, Aluno):
            return False
        return self.matricula == other.matricula

    def __hash__(self):
        return hash(self.matricula)


class Externo(Usuario):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, "Externo")
        self.cpf = cpf

    def __eq__(self, other):
        if not isinstance(other, Externo):
            return False
        return self.cpf == other.cpf

    def __hash__(self):
        return hash(self.cpf)