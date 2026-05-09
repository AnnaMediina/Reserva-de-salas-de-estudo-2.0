class Usuario:
    def __init__(self, nome: str, vinculo: str):
        self.nome = nome
        self.vinculo = vinculo

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