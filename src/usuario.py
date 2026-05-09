from observer import Observer

class Usuario(Observer):
    def __init__(self, nome: str, vinculo: str):
        self.nome = nome
        self.vinculo = vinculo
        
    def update_push(self, msg: str, dados: dict = None):
        print(f"\n[notificacao PUSH para {self.nome}] {msg}")
        if dados:
            print(f"-Dados enviados ativamente: {dados}")

    def update_pull(self, subject):
        print(f"\n[notificacao PULL para {self.nome}], algo mudou na sua reserva!")
        estado_atual = subject.obter_estado()
        print(f" -att. os dados. Status é '{estado_atual['status']}'")
    def __str__(self):
        return f"{self.nome} ({self.vinculo})"


class Professor(Usuario):
    def __init__(self, nome: str, identificador: str):
        super().__init__(nome, "Professor")
        self.identificador = identificador


class Aluno(Usuario):
    def __init__(self, nome: str, matricula: str):
        super().__init__(nome, "Aluno")
        self.matricula = matricula


class Externo(Usuario):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, "Externo")
        self.cpf = cpf