from Observer import Observer

class Usuario(Observer): 
    def __init__(self, nome, email, vinculo, id):
        self.nome = nome
        self.email = email
        self.vinculo = vinculo
        self.id = id

    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getVinculo(self):
        return self.vinculo
    
    def getId(self):
        return self.id

    def update(self, sala, acao):
        print(f"Reserva da sala {sala.getNumero()} foi {acao}.")

class Professor(Usuario):
    def __init__(self, nome, email, vinculo, id, departamento):
        super().__init__(nome, email, vinculo, id)
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento
    

class Aluno(Usuario):
    def __init__(self, nome, email, vinculo, id, curso):
        super().__init__(nome, email, vinculo, id)
        self.curso = curso

    def getCurso(self):
        return self.curso
    
class Externo(Usuario):
    def __init__(self, nome, email, vinculo, id, instituicao):
        super().__init__(nome, email, vinculo, id)
        self.instituicao = instituicao

    def getInstituicao(self):
        return self.instituicao
